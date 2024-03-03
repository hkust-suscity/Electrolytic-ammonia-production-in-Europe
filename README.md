# Electrolytic-Ammonia-Production-in-Europe
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10771014.svg)](https://doi.org/10.5281/zenodo.10771014)


Welcome to the official GitHub repository for the research article _"Effects of emissions caps on the costs and feasibility of low-carbon hydrogen in the European ammonia industry"_, currently under review at _Nature Communications_.

This repository hosts the codebase that accompanies our research article, the impact of decarbonization targets for hydrogen synthesis on the economic viability and technical feasibility of retrofitting existing European ammonia plants for on-site, semi-islanded electrolytic hydrogen production.

## Abstract

_The European ammonia industry is responsible for 36 Mt of carbon dioxide per year, primarily due to hydrogen production from steam methane reforming (SMR). These emissions can be mitigated by producing hydrogen via water electrolysis powered by dedicated renewable energy sources with grid backup to maintain continuous plant operations. This study investigates the impact of decarbonization targets for hydrogen synthesis on the economic viability and technical feasibility of retrofitting existing European ammonia plants for on-site, semi-islanded electrolytic hydrogen production. Results show that electrolytic hydrogen cuts emissions, on average, by 85% (36%-100% based on grid price and carbon intensity from 2025 to 2050), even without enforcing any emission limit. However, an optimal lifespan average well-to-gate emission cap of 1 kg carbon dioxide equivalent (CO2e)/kg H2 achieves even deeper emissions reduction of 95% (92%-100%) while maintaining cost-competitiveness with SMR in renewable-rich regions (mean levelized cost of hydrogen produced from 2025 to 2050 or LCOH: 4.1 EUR/kg H2). Conversely, a 100% emissions reduction target dramatically increases costs (mean LCOH: 6.3 EUR/kg H2) and land area for renewables installations, likely hindering the transition to electrolytic hydrogen in regions with poor renewables and limited land. Increasing plant flexibility is an effective strategy to reduce costs, particularly in off-grid plants (mean reduction: 32%). This work guides policymakers in defining cost-effective decarbonization targets and identifying region-based strategies to support an electrolytic hydrogen-fed ammonia industry._

## Repository Structure

- `EMHIRES_analysis`: Contains code and dataframes for a detailed analysis of capacity factors for solar and wind energy production in Europe, utilizing the EMHIRES[^1][^2] dataset.
- `GBM_MCS_model`: Includes code and dataframes for forecasting industrial electricity prices in Europe until 2050, employing Geometric Brownian Motion and Monte Carlo simulations.
- `optimization_model`: Houses code and dataframes for modeling and optimizing the retrofitting process for European ammonia plants.


### Additional Documentation

- `NOMENCLATURE.md`: Offers a comprehensive glossary of symbols, indices, sets, and terms utilized throughout the research.

- `INPUT_PARAMETERS_METADATA.xlsx`: Contains a detailed Excel spreadsheet presenting the input parameters utilized in the analysis. This spreadsheet includes the names of variables, units of measure, values utilized for sensitivity analysis, and explanatory notes to aid in the interpretation and replication of the research.

## Prerequisites

The model is developed using Python 3.9.12 in the JupyterLab 3.3.2 environment. Ensure that you have Gurobi Optimizer version 10.0.1 installed before running the script. Refer to the [Gurobi Installation Guide](https://www.gurobi.com/documentation/) for setup instructions and license activation.

## How to Use

To run the code provided in this repository:

1. Clone the repository to your local machine.
2. Install the required Python version and the JupyterLab environment.
3. Set up Gurobi Optimizer and activate your license.
4. Navigate to the desired code or data folder.
5. Open the Jupyter notebook or Python file and execute the code.

## Contact Information

For inquiries, data requests, or feedback, please [contact us](mailto:).

## Authors and Affiliations

Authors and affiliations will be updated upon article acceptance.

## Corresponding Author

Details of the corresponding author will be provided upon article acceptance.

[^1]: EMHIRES part 1 --> https://op.europa.eu/en/publication-detail/-/publication/85b2dc7f-aa61-11e6-aab7-01aa75ed71a1/language-en  
[^2]: EMHIRES part 2 --> https://op.europa.eu/en/publication-detail/-/publication/a6c0cf55-45aa-11e7-aea8-01aa75ed71a1/language-en

