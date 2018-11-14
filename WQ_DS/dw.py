import pandas as pd
import numpy as np
import gzip

with gzip.open('./dw-data/201701scripts_sample.csv.gz', 'rb') as f:
    scripts_data = pd.read_csv(f) #read_csv returns a data frame

scripts =  scripts_data

print (scripts.head())


with gzip.open('./dw-data/practices.csv.gz', 'r') as p:
    col_names=[ 'code', 'name', 'addr_1', 'addr_2', 'borough', 'village', 'post_code']    
    practice_data = pd.read_csv(p, names = col_names, header = None)
    


practices = practice_data

print (practices.head())

with gzip.open('./dw-data/chem.csv.gz', 'rb') as c:
    chem_data = pd.read_csv(c)

chem = chem_data

print (chem.head())   


#Question 1: summary_statistic


print ("Describe scripts: \n", scripts.describe())
print ("Describe practice: \n",practices.describe())
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
    #get rid of irrelevant columns in practice, only keep 'code' and 'post_code'
    practice_filtered = practices.drop(['name','addr_1','addr_2','borough','village'], axis =1)
    joined = pd.merge(scripts,practice_filtered, how='inner', left_on = 'practice', right_on = 'code')
    print ("scripts inner join practice: ")
    print (joined)
    #group joined by bnf_name and post_code
    item_by_region = joined.groupby(['post_code','bnf_name'])['items'].sum().reset_index()
    print ("joined group by post_code and bnf_name and sum by items:")
    print (item_by_region)
    
    #get max bnf_name in each post code
    max_items = item_by_region.loc[item_by_region.groupby('post_code')['items'].idxmax()]
    
    print ("max bnf name in each post code: ")
    print (max_items)
items_by_region()