# Electrolysis Hydrogen Planning Analysis for Ammonia Plants In EU Github page

This is the official code repository for the research article (cite name paper) in preparation for submission.

In this article we study the decarbonization of the European ammonia sector through the substitution of gray hydrogen with green hydrogen produced in-loco.

The model is developed using Python 3.9.12 in the JupyterLab 3.3.2 environment.

### 1. Content
The repository is divided into two folders:
- `sample_code` containts the sample codes (`Code_hydrogen_paper.ipynb` and `Code_hydrogen_paper.py`), simplified version of the code used to obtain the main result of the article in preparation for submission. 
- `sample_database` containts instead the sample datasets to run the code. `input_table_sample` presents the value of the input parameters used in the optimization model, while `EMHIRES_dataset_sample` contains a sample of the EMHIRES[^1][^2] dataset providing 1-year hourly PV and wind turbine capacity factors. 

Lastly, the document `METADATA.md` presents all the information required to undestand the key parameters and variables of the model.


### 2. Contacts
For any queries, data request and feedback contact Stefano Mingolla: smingolla@connect.ust.hk or smingolla@ethz.ch. 

### 3. Data Availability

The code and datasets provided are simplified version of the material used in the article (mention). The purpose of the sample code is to highlight the mechanisms of the developed model. Sample data and code referred to the following 4 regions: 
- `ES42`, Castile-La Mancha (Spain),
- `ITH5`, Ferrara (Italy),
- `NO03`, Sør-Østlandet (Norway),
- `UKC1`, Tees Valley and Durham (United Kingdom).

All the data and complete code related to this paper may be requested from the corresponding authors (cite). 

[^1]: EMHIRES part 1 --> https://op.europa.eu/en/publication-detail/-/publication/85b2dc7f-aa61-11e6-aab7-01aa75ed71a1/language-en  
[^2]: EMHIRES part 2 --> https://op.europa.eu/en/publication-detail/-/publication/a6c0cf55-45aa-11e7-aea8-01aa75ed71a1/language-en
