import pandas as pd
import numpy as np
import gzip

with gzip.open('./dw-data/201701scripts_sample.csv.gz', 'rb') as f:
    scripts_data = pd.read_csv(f)

scripts =   pd.DataFrame(scripts_data)  

print (scripts)


with gzip.open('./dw-data/practices.csv.gz', 'rb') as f:
    practice_data = pd.read_csv(f)
    
practices = pd.DataFrame(practice_data)
print (practices)

with gzip.open('./dw-data/chem.csv.gz', 'rb') as f:
    chem_data = pd.read_csv(f)

chem = pd.DataFrame(chem_data) 

print (chem)   


#Question 1: summary_statistic

print (scripts.describe(percentiles, include, exclude))