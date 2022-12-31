# Import libraries
import pandas as pd
import numpy as np
from scipy.optimize import differential_evolution
from scipy.optimize import minimize
from scipy.optimize import Bounds


# Import dataframes
# Import input parameter dataframe
df = pd.read_excel(r'input_table_sample.xlsx')
df.set_index("Input_parameters", inplace = True)

# Import EMHIRES dataframe
df_EMHIRES = pd.read_csv(r'EMHIRES_dataset_sample.csv', index_col = 0) 


# Select scenario
pessimistic = True
average = False
optimistic = False

if pessimistic == True:
    scenario = "pes"
elif average == True:
    scenario = "avg"
else:
    scenario = "opt"
    

# Select emission threshold
zero_kg = False # 0 kg CO2/kg H2
one_kg = False # 1 kg CO2/kg H2
zero_five_kg = False # 0.5 kg CO2/kg H2
zero_one_kg = False # 0.1 kg CO2/kg H2
nine_five_kg = True # 9.5 kg CO2/kg H2

if zero_kg == True: 
    threshold = 0
elif one_kg == True:
    threshold = 1
elif zero_five_kg == True:
    threshold = 0.5
elif zero_one_kh == True:
    threshold = 0.1
else:
    threshold = 9.5 


# Choose NUTS-2 level region to analyze
# Note, in this test code you can choose within the following 4 regions: ES42, ITH5, NO03, UKC1
CHOOSE_REGION = "ITH5"
for i in ["ES","IT","NO","UK"]:
    if CHOOSE_REGION.startswith(i):
        COUNTRY = i


# Define energy balance
def calculate_energy_balance(i,dataset, IC_PV, IC_WT, IC_HGU_WE, IC_batt,IC_comp, IC_h2stor, En_stor_batt, kg_stor_h2, En_comp, En_HGU_WE, Dh_H2):

# Import capacity factor PV and WT from EMHIRES sample dataset "df_EMHIRES"
    CF_PV = dataset.at[i, f'{CHOOSE_REGION}PV']
    CF_WT = dataset.at[i, f'{CHOOSE_REGION}WT']

# Calculate the hourly renewable energy input to the system
    En_PV = IC_PV * CF_PV 
    En_WT = IC_WT * CF_WT 
    En_total = En_PV + En_WT #energy from solar PV + WT
    En_grid = 0
# Calculate hourly energy demand for the Ammonia plant
    En_plant = Dh_H2 * En_HGU_WE #hourly energy required to synthesize 7.5 tons of H2
    IC_HGU_WE_kg = IC_HGU_WE/En_HGU_WE  # Electrolyzer installed capacity converted to effective kgs of H2
    En_after_H2_production = En_total - En_plant
    
    # The main if loop!
    # Case 1: we have an energy surplus in hour t
    if En_total >= En_plant:
        Free_capacity_batteries = IC_batt - En_stor_batt #capacity batteries unutilized and available for energy storage
        
        # Next, store the energy surplus in the battery 
        if En_after_H2_production <= Free_capacity_batteries:  #check not fully charged 
            En_stor_batt += En_after_H2_production
            En_after_battery = 0
        else:  # battery is filled during the charging process
            En_stor_batt = IC_batt
            En_after_battery = En_after_H2_production - FREECAP_battery
            Kg_H2_remaining = En_after_battery/(En_HGU_WE+En_comp)      # the total number of kgs of h2 that could still be produced after charging the battery 
            
            if min(IC_HGU_WE_kg-Dh_H2,IC_comp, IC_h2stor-kg_stor_h2) - Kg_H2_remaining >= 0:  # there is enough electrolyzer, compressor, tank capacity to transform the energy surplus into hydrogen to store
                kg_stor_h2 += Kg_H2_remaining
            else:  # there is insufficient free space in tanks or capacity in the compressors or electrolyzer for H2 conversion and storage
                kg_stor_h2 += min(IC_HGU_WE_kg-Dh_H2,IC_comp, IC_h2stor-kg_stor_h2)
                # Waste any remaining energy.
      
    # Case 2: we have an energy deficit in hour t (i.e En_total < En_plant)
    else:   
        # use as much energy as possible from renewables for H2 production
        En_remaining_for_H2_production = En_plant - En_total
        # Then. Empty H2 storage tanks first
        if kg_stor_h2 > En_remaining_for_H2_production/En_HGU_WE:
            kg_stor_h2 = kg_stor_h2 - (En_remaining_for_H2_production/En_HGU_WE)
            En_remaining_for_H2_production = 0
        else: 
            En_remaining_for_H2_production = En_remaining_for_H2_production - (kg_stor_h2*En_HGU_WE) 
            kg_stor_h2 = 0
            # Then discharge battery to produce additional hydrogen
            if En_stor_batt >= En_remaining_for_H2_production:
                En_stor_batt = En_stor_batt - En_remaining_for_H2_production
                En_remaining_for_H2_production = 0
            else:
                En_remaining_for_H2_production = En_remaining_for_H2_production - En_stor_batt
                En_stor_batt = 0
                # The rest comes from the grid
                En_grid += En_remaining_for_H2_production

       
    return En_stor_batt, kg_stor_h2, En_grid, En_total, En_PV, En_WT


# define LCOH
def calculate_capex(IC_PV, IC_WT, IC_HGU_WE, IC_batt, IC_comp, IC_h2stor, En_frac_grid, En_total, kg_stor_h2):
    # Utility-scale solar PV 
    A_tot = A_PV * IC_PV
    CAPEX_land = land_price * A_tot
    CAPEX_PV = cost_PV_i * IC_PV
    capex_PV = (CAPEX_PV + CAPEX_land)
    opex_PV = CAPEX_PV + cost_M_PV * 28
    # ALK electrolyzer
    CAPEX_HGU_WE = cost_HGU_WE * IC_HGU_WE
    capex_HGU_WE = CAPEX_HGU_WE * (1 + Bld_prj)  
    opex_HGU_WE = CAPEX_HGU_WE * L_HGU_WE * cost_M_HGU_WE 
    # Utility-scale wind turbines
    A_tot_WT = A_WT * IC_WT
    CAPEX_land_WT = land_price * A_tot_WT
    CAPEX_WT = cost_WT_i * IC_WT
    capex_WT = (CAPEX_WT + CAPEX_land_WT)
    opex_WT = CAPEX_WT + cost_M_WT * 28
    # Utility-scale Li-ion battery for electricity storage
    capex_batt = IC_batt * cost_batt
    opex_batt = (capex_batt * L_batt_1 * cost_M_batt) 
    # Dedicated tanks for compressed H2 storage
    capex_h2stor = IC_h2stor * cost_h2stor
    # Dedicated utility-scale H2 compressor
    capex_comp = IC_comp * cost_comp
    opex_comp = (capex_comp * L_batt_1 * cost_M_batt) 
    #cost of grid electricity
    if En_frac_grid * En_HGU_WE * CE_el_i <= threshold:
        cost_el_g = (price_el_g_i * En_frac_grid * En_HGU_WE * Dh_H2 * 8760 * 28)
    # Carbon intensity grid electricity
        CE_WE = (CE_el_i * En_frac_grid * En_HGU_WE * Dh_H2 * 8760 * 28) 
        ct_WE = CE_WE * CT_i
    else:
        cost_el_g = 1E15
        CE_WE = 1E15
        ct_WE = CE_WE * CT_i
    #LCOH
    LCOH = ((capex_PV + capex_HGU_WE + capex_WT + capex_batt + capex_h2stor + capex_comp) + (opex_HGU_WE + capex_WT + opex_comp) + cost_el_g + ct_WE)/(Dh_H2 * 8760 * 28)
    
    return LCOH


#define variables
# Hourly H2 demand
Dh_H2 = float(df.loc[f"Dh_H2"]["Fixed"])
# Dedicated utility-scale H2 compressor
cost_comp = float(df.loc[f"cost_comp"]["Fixed"])
En_comp = float(df.loc[f"En_comp"]["Fixed"])
cost_M_comp = float(df.loc[f"cost_M_comp"]["Fixed"])
# Dedicated tanks for compressed H2 storage
cost_h2stor = float(df.loc[f"cost_h2stor"]["Fixed"])
# Utility-scale Li-ion battery for electricity storage
cost_batt = float(df.loc[f"cost_batt_{scenario}"]["Fixed"])
L_batt = float(df.loc[f"L_batt"]["Fixed"]) 
cost_M_batt = float(df.loc[f"cost_M_batt"]["Fixed"])
# land price
land_price = float(df.loc[f"land_price"][CHOOSE_REGION])
# Project costs for utility-scale electrolyzer installation
Bld_prj = float(df.loc[f"Bld_prj"]["Fixed"])
# Utility-scale solar PV 
cost_PV_i = float(df.loc[f"cost_PV_i_{scenario}"][COUNTRY]) 
A_PV = float(df.loc[f"A_PV"]["Fixed"])
cost_M_PV = float(df.loc[f"cost_M_PV_{scenario}"]["Fixed"]) 
# Utility-scale wind turbines
cost_WT_i = float(df.loc[f"cost_WT_i_{scenario}"][COUNTRY])
A_WT = float(df.loc[f"A_WT"]["Fixed"])
cost_M_WT = float(df.loc[f"cost_M_WT_{scenario}"]["Fixed"])
# ALK electrolyzer
cost_HGU_WE = float(df.loc[f"cost_HGU_WE_{scenario}_ALK"]["Fixed"])  
En_HGU_WE = float(df.loc[f"En_HGU_WE_{scenario}_ALK"]["Fixed"])
cost_M_HGU_WE = float(df.loc[f"cost_M_HGU_WE_{scenario}"]["Fixed"])
L_HGU_WE = float(df.loc[f"L_HGU_WE_ALK"]["Fixed"])
# EU-ETS
CT_i = float(df.loc[f"CT_i_{scenario}"]["Fixed"])
# Price grid electricity
price_el_g_i = float(df.loc[f"price_el_g_i_{scenario}"][COUNTRY]) 
# Carbon intensity grid electricity
CE_el_i = float(df.loc[f"CE_el_i_{scenario}"][COUNTRY]) 


# Define optimization
def LCOH_optimization_test(x):
    # pull variables from input array
    print("new iteration")
    IC_PV = x[0]
    IC_WT = x[1]
    IC_HGU_WE = x[2]
    IC_batt = x[3]
    IC_comp = x[4]
    IC_h2stor = x[5]

    En_stor_batt = 0 # initial condition
    kg_stor_h2 = 0 #initial condition
    
    En_stor_batt_arr, kg_stor_h2_arr, En_grid_arr, En_total_arr, En_PV_arr, En_WT_arr = [], [] , [] , [], [], []

    # Check if there is enough electrolyzer installed capacity to satisfy the hourly demand of H2
    if Dh_H2 * En_HGU_WE <= IC_HGU_WE: 
        for i in range(1,len(df_EMHIRES)):

            batt,tank,grid,total,PV,WT= calculate_energy_balance(i,df_EMHIRES, IC_PV, IC_WT, IC_HGU_WE, IC_batt, IC_comp, IC_h2stor, En_stor_batt, kg_stor_h2, En_comp, En_HGU_WE, Dh_H2)
    
            En_stor_batt_arr = np.append(En_stor_batt_arr, batt)
            kg_stor_h2_arr = np.append(kg_stor_h2_arr, tank)
            En_grid_arr = np.append(En_grid_arr, grid)
            En_total_arr = np.append(En_total_arr,total)
            En_PV_arr = np.append(En_PV_arr,PV)
            En_WT_arr = np.append(En_WT_arr,WT)

            En_stor_batt = batt
            kg_stor_h2 = tank

    else:
        print("Error: Installed electrolyzer capacity is insufficient to meet plant demand.")
        print(f"For this value of Dh_H2, installed capacity must be at least {En_HGU_WE * Dh_H2} MW")
    
    En_frac_grid = np.sum(En_grid_arr)/(np.sum(En_total_arr) + np.sum(En_grid_arr))
    En_total = np.sum(En_total_arr)
    En_PV = np.sum(En_PV_arr)
    En_WT = np.sum(En_WT_arr)
    kg_stor_h2 = np.sum(kg_stor_h2_arr)

    LCOH = calculate_capex(IC_PV, IC_WT, IC_HGU_WE, IC_batt, IC_comp, IC_h2stor, En_frac_grid, En_total, kg_stor_h2)

    print(f"LCOH = {LCOH}")
    print(f"IC_PV = {IC_PV}")
    print(f"IC_WT = {IC_WT}")
    print(f"IC_HGU_WE = {IC_HGU_WE}")
    print(f"IC_batt = {IC_batt}")
    print(f"IC_comp = {IC_comp}")
    print(f"IC_h2stor = {IC_h2stor}")
    print(f"En_frac_grid = {En_frac_grid}")
        
    return LCOH
    


#first round of Differential Evolution (DE)
min_ele_size = Dh_H2*En_HGU_WE

bounds = Bounds([0,0,min_ele_size,0,0,0],[1E4,5E3,5E3,5E4,5E4,1E6])

LCOH_vals = []
res = differential_evolution(LCOH_optimization_test, bounds=bounds, popsize = 10)


#second round of Nelder-Mead using the results of the DE as "best guess" for the second optimization
bounds = Bounds([0,0,min_ele_size,0,0,0],[1E10,1E10,1E10,1E10,1E10,1E10])
x0 = np.array(res.x)

LCOH_vals = []
res = minimize(LCOH_optimization_test, x0, method='nelder-mead', bounds=bounds, tol = 1E-15)


res.x

# IC_PV
print(f"IC_PV = {res.x[0]} MW")
# IC_WT
print(f"IC_WT = {res.x[1]} MW") 
# IC_HGU_WE (Electrolyzer)
print(f"IC_HGU_WE = {res.x[2]} MW")
# IC_batt
print(f"IC_batt = {res.x[3]} MWh")
# IC_comp
print(f"IC_comp = {res.x[4]} kg H2/hr")
# IC_h2stor
print(f"IC_H2_stor = {res.x[5]} kg H2")
# LCOH
print(f"minimum LCOH = {res.fun} EUR/kg")


df_results = pd.DataFrame({"LCOH":[res.fun], "IC_PV":[res.x[0]], "IC_WT":[res.x[1]], "IC_HGU_WE":[res.x[2]], "IC_batt":[res.x[3]], "IC_comp":[res.x[4]], "IC_H2_stor":[res.x[5]]}, index = [CHOOSE_REGION])
df_results
