# JEM217: final-empirical-project
This is repository serves as the supportive tool for conducting final empirical project.

1.) It is hosting Python code used to dowload data from [sreality](https://www.sreality.cz/) using its public [API](https://www.sreality.cz/api/cs/v2/estates?). Raw data are downloaded in download.py using functions from functions_all and saved into estate_data.sqlite.

2.) Moreover, Python cleaning code can be found in cleaning.ipynb which cleans the raw data and save them into data.csv and output excel files (same data) which are prepared dataframes for the econometrical analysis conducted in R (not in this repository).
