# Nomenclature

This document outlines the nomenclature used in the research and the accompanying codebase. The following symbols and indices are utilized to model the economic and technical aspects of the transition to low-carbon hydrogen in the European ammonia industry.

## Indices

- `t`: Index for time-steps – hours, t ∈{0,1,…,T} with T=8760 (hours in a year)
- `l`: Index for years, l ∈{0,1,…,L} with L=25 years

## Sets

- `J`: Set of energy carriers
- `K`: Set of technologies

## Energy Carriers

- `E`: Electricity
- `H_2`: Hydrogen
- `N_2`: Nitrogen
- `NH_3`: Ammonia

## Technologies

- `PV`: Photovoltaic (solar panels)
- `WT`: Wind Turbine
- `EL`: Electrolyzer (for hydrogen production)
- `A`: Air Separator Unit
- `S`: Ammonia Synthesis Loop (Synloop)
- `CP`: Hydrogen Compressor
- `ST`: Hydrogen High-Pressure Storage Tank
- `B`: Battery Energy Storage System

## Parameters

- `Ω`: Capacity factor for renewable energies
- `s`: Solar data (irradiance, availability)
- `w`: Wind data (speed, availability)
- `D`: System output demand or requirement
- `p`: Price of energy carriers
- `γ`: Carbon footprint associated with energy grids and technologies
- `c`: Investment cost for technology
- `v`: Operation and maintenance (O&M) cost for technology
- `η`: Performance efficiency of technology

## Variables

- `U`: Input energy to a technology/process
- `V`: Output energy from a technology/process
- `M`: Imported electricity from the grid
- `P`: Size/capacity of technology
- `b`: Binary variable for technology selection (1 if selected, 0 otherwise)
- `y`: ON/OFF scheduling variable for technologies (1 if ON, 0 if OFF)
