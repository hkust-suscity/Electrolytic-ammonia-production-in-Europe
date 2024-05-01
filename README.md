# Effects of emissions caps on the costs and feasibility of low-carbon hydrogen in the European ammonia industry
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10771014.svg)](https://doi.org/10.5281/zenodo.10771014)


Welcome to the official GitHub repository for the research article "Effects of emissions caps on the costs and feasibility of low-carbon hydrogen in the European ammonia industry", accepted for publication in Nature Communications on 19 April 2024:\
[DOI: 10.1038/s41467-024-48145-z](https://doi.org/10.1038/s41467-024-48145-z) 

This repository contains all data, code, and references necessary to replicate the main results reported in our research article.

## Abstract

_The European ammonia industry emits 36 million tons of carbon dioxide annually, primarily from steam methane reforming (SMR) hydrogen production. These emissions can be mitigated by producing hydrogen via water electrolysis using dedicated renewables with grid backup. This study investigates the impact of decarbonization targets for hydrogen synthesis on the economic viability and technical feasibility of retrofitting existing European ammonia plants for on-site, semi-islanded electrolytic hydrogen production. Results show that electrolytic hydrogen cuts emissions, on average, by 85% (36%-100% based on grid price and carbon intensity), even without enforcing emission limits. However, an optimal lifespan average well-to-gate emission cap of 1 kg carbon dioxide equivalent (CO2e)/kg H2 leads to a 95% reduction (92%-100%) while maintaining cost-competitiveness with SMR in renewable-rich regions (mean levelized cost of hydrogen (LCOH) of 4.1 euro/kg H2). Conversely, a 100% emissions reduction target dramatically increases costs (mean LCOH: 6.3 euro/kg H2) and land area for renewables installations, likely hindering the transition to electrolytic hydrogen in regions with poor renewables and limited land. Increasing plant flexibility effectively reduces costs, particularly in off-grid plants (mean reduction: 32%). This work guides policymakers in defining cost-effective decarbonization targets and identifying region-based strategies to support an electrolytic hydrogen-fed ammonia industry._

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

For inquiries, data requests, or feedback, please [contact us](mailto:smingolla@connect.ust.hk).

## Authors and Affiliations

Contributors:

- Stefano Mingolla<sup>1*</sup>
- Paolo Gabrielli<sup>2,3†</sup>
- Alessandro Manzotti<sup>4,5†</sup>
- Matthew J. Robson<sup>4†</sup>
- Kevin Rouwenhorst<sup>6,7,8</sup>
- Francesco Ciucci<sup>4,9</sup>
- Giovanni Sansavini<sup>2</sup>
- Magdalena M. Klemun<sup>10,11*</sup>
- Zhongming Lu<sup>1,10*</sup>

1. Division of Environment and Sustainability, Hong Kong University of Science and Technology, Clear Water Bay, Kowloon, Hong Kong SAR, China
2. Institute of Energy and Process Engineering, ETH Zurich, 8092, Zurich, Switzerland
3. Department of Global Ecology, Carnegie Institution for Science, Stanford, CA 94305, USA
4. Department of Mechanical and Aerospace Engineering, Hong Kong University of Science and Technology, Clear Water Bay, Kowloon, Hong Kong SAR, China
5. Department of Physics, Technical University of Denmark, Kongens Lyngby, Denmark
6. Ammonia Energy Association, 77 Sands Street, Brooklyn, NY 11201, USA
7. Catalytic Processes & Materials, MESA+ Institute for Nanotechnology, Department of Science & Technology, University of Twente, P.O. Box 217, 7500 Enschede, The Netherlands
8. Koolen Industries, Europalaan 202, 7553 SC Hengelo, The Netherlands
9. Chair of Electrode Design for Electrochemical Energy Systems, University of Bayreuth, 95448 Bayreuth, Germany
10. Energy Institute, The Hong Kong University of Science and Technology, Hong Kong SAR, China
11. Division of Public Policy, Hong Kong University of Science and Technology, Clear Water Bay, Kowloon, Hong Kong SAR, China

## Corresponding Author

- Stefano Mingolla: smingolla@connect.ust.hk
- Magdalena M. Klemun: magdalena@ust.hk
- Zhongming Lu: zhongminglu@ust.hk

[^1]: EMHIRES part 1 --> https://op.europa.eu/en/publication-detail/-/publication/85b2dc7f-aa61-11e6-aab7-01aa75ed71a1/language-en  
[^2]: EMHIRES part 2 --> https://op.europa.eu/en/publication-detail/-/publication/a6c0cf55-45aa-11e7-aea8-01aa75ed71a1/language-en

