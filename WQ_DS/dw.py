import pandas as pd
import numpy as np
import gzip
import logging

from math import sqrt

pd.set_option('display.max_columns', None)
pd.set_option('expand_frame_repr', False)

logging.basicConfig(filename='dw.log', level=logging.DEBUG)


with gzip.open('./dw-data/201701scripts_sample.csv.gz', 'rb') as f:
    scripts_data = pd.read_csv(f) #read_csv returns a data frame

scripts =  scripts_data
print ("SCRIPT:")
print (scripts.head())


with gzip.open('./dw-data/practices.csv.gz', 'r') as p:
    col_names=[ 'code', 'name', 'addr_1', 'addr_2', 'borough', 'village', 'post_code']    
    practice_data = pd.read_csv(p, names = col_names, header = None)
    
practices = practice_data
print ("PRACTICE:")
print (practices.head())

with gzip.open('./dw-data/chem.csv.gz', 'rb') as c:
    chem_data = pd.read_csv(c)

chem = chem_data
print ("CHEM:")
print (chem.head())   


#Question 1: summary_statistic


print ("Describe scripts: \n", scripts.describe())
print ("Describe practice: \n",practices.describe())
def summary_stats():
    results = []
    
    temp = scripts.describe()
    
    print ("COLUMNS: " + temp.columns)
    
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
    #since a practice can have multiple post codes, we have to sort them  by alphabet and drop the duplicates
    practices_sorted = practices.sort_values('post_code').drop_duplicates('code')
    print ("practice sorted and drop duplicates:")
    print (practices_sorted)
    
    #get rid of irrelevant columns in practice, only keep 'code' and 'post_code'
    practice_filtered = practices_sorted.drop(['name','addr_1','addr_2','borough','village'], axis =1)
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
    
    #Total items in each post code
    total_items_post_code = joined.groupby('post_code')['items'].sum().reset_index()
    print ("total items in each post code")
    print (total_items_post_code)
    
    # merge total_items_post_code with max_items again to make use both of them
    merged = pd.merge(max_items,total_items_post_code, how='inner', left_on ='post_code', right_on ='post_code' ).sort_values('post_code')
    print ("Merge max_items and total_items_post_code on post_code ")
    print (merged)
    
    #get the fraction: max_items / total_items
    merged['fraction'] = merged['items_x'] / merged['items_y']
    print ("Merged after calculating the fraction")
    print (merged)
    
    #get a df that contain only required items and
    final_df = merged.groupby(['post_code','bnf_name'])['fraction'].sum().reset_index()
    print ("final data frame")
    print (final_df)
    
    #final answer
    tuples = [tuple(x) for x in final_df.values][:100]
    print ("final answer")
    print (tuples)
    
    return tuples
    
items_by_region()

# DW 4: Script Anomalies
print ("DW 4: Script Anomalies")
chem_copy = chem.drop_duplicates(subset='CHEM SUB')
opioids = ['morphine', 'oxycodone', 'methadone', 'fentanyl', 'pethidine', 'buprenorphine', 'propoxyphene', 'codeine']
pattern = '|'.join(opioids)
print ("Pattern", pattern)

# Add a new column to flag chem with opioid
chem_copy['flag_opioid'] = chem_copy['NAME'].str.contains(pattern, case = False)

# join with scripts                    
scripts_joined_chem = pd.merge(scripts, chem_copy, how='left', left_on='bnf_code', right_on='CHEM SUB')
scripts_joined_chem['flag_opioid'] = scripts_joined_chem['flag_opioid'].fillna(False)
print ("Scripts inner join chem with opioid:")
print (scripts_joined_chem)

# group by practice and take the mean of opioid flag
OVERALL_RATE = scripts_joined_chem['flag_opioid'].mean()
print ("OVERALL_RATE:")
print (OVERALL_RATE)

opioid_scores = scripts_joined_chem.groupby('practice')['flag_opioid'].mean().reset_index()
opioid_scores.columns = ['practice','mean']

def relative_value(mean):
    return abs(mean - OVERALL_RATE) 

# subtract the opio_rate per practice from the overall
opioid_scores['relative'] = opioid_scores['mean'].apply(relative_value)
# get the total prescription per practice
print ("SIZE:")
temp = scripts_joined_chem.groupby(['practice']).size()
temp2 = pd.DataFrame(temp)
temp2.columns =['n_pres']
temp2.reset_index(level = 0, inplace = True)

opioid_scores = pd.merge(opioid_scores, temp2, how='inner', left_on ='practice', right_on = 'practice')
opioid_scores['sqrt_n_pres'] = opioid_scores['n_pres'].apply(sqrt)

# standard deviation across all practice

SIGMA = pd.DataFrame(scripts_joined_chem.groupby('practice')['flag_opioid'].std())
SIGMA.reset_index(level=0,  inplace = True)
SIGMA.columns = ['practice', 'sigma']

opioid_scores = pd.merge(opioid_scores, SIGMA, how='inner', left_on ='practice', right_on = 'practice')


print ("Standard deviation of opioid across all practice")
print (SIGMA)

# standard error
opioid_scores['sdt_error'] = opioid_scores['sigma'] / opioid_scores['sqrt_n_pres']

# z score
opioid_scores['z_score'] = opioid_scores['relative'] / opioid_scores['sdt_error']


print ("opioid_rate_per_practice")
print (opioid_scores)
