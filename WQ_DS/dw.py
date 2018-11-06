import pandas as pd
import numpy as np
import gzip

with gzip.open('./dw-data/201701scripts_sample.csv.gz', 'rb') as f:
    scripts_data = pd.read_csv(f)

scripts =   pd.DataFrame(scripts_data)  

print (scripts.head())


with gzip.open('./dw-data/practices.csv.gz', 'rb') as p:
    practice_data = pd.read_csv(p)
    
practices = pd.DataFrame(practice_data)
print (practices.head())

with gzip.open('./dw-data/chem.csv.gz', 'rb') as c:
    chem_data = pd.read_csv(c)

chem = pd.DataFrame(chem_data) 

print (chem.head())   


#Question 1: summary_statistic


print ("Describe scripts: \n", scripts.describe())

def summary_stats():
    results = []
    
    temp = scripts.describe()
    
    print ("columns: " + temp.columns)
    
    for key in temp.columns:
        #print ("column name: " ,key, "| row index: ", temp[key].index)
        total = scripts[key].sum()
        avg = float(total) / temp[key]['count']
        std = temp[key]['std']
        q25 = temp[key]['25%']
        med = temp[key]['50%']
        q75 = temp[key]['75%']
        
        t = (total, avg, std , q25, med, q75)
        print ("Scripts stats: ", (key,t))
        results.append((key, t))
    
    return results    
    
summary_stats()


# Question 2: Most common item
def most_common_item():
    
    temp = scripts.groupby('bnf_name')['items'].sum() #group by bnf_name then take sum of items in each group
    print ("Max bnf_name/items: ", temp.idxmax(), temp.max()) #get the index of the row with max items
    return [(temp.idxmax(), temp.max())]

most_common_item()

# Question 3: Items by region
def items_by_region():
    joined = pd.merge(scripts,practices, how='inner', left_on = 'practice', right_on = 'A81001')
    print (joined)
    
items_by_region()