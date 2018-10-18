import gzip
import simplejson as json
from math import sqrt

with gzip.open('./pw-data/201701scripts_sample.json.gz', 'rb') as f:
    scripts = json.load(f)

with gzip.open('./pw-data/practices.json.gz', 'rb') as f:
    practices = json.load(f)

#1 Summary Statistics

def describe(key):
    
    key_list = ['items', 'quantity', 'nic', 'act_cost']
    value_list = []
    
    total = 0
    avg = 0
    s = 0
    q25 = 0
    med = 0
    q75 = 0
    
    if (key in key_list ):
        
        #make the list of the item's value
        for script in scripts:
            value_list.append(script[key])
            
        #sort the list    
        value_list.sort(key=None, reverse=False)
        value_list_len = len(value_list)
        
        #sum
        total = float(sum(value_list))
        
        #mean
        avg = total / value_list_len 
        
        #variance 
        delta_sum = 0
        for value in value_list:
            delta_sum = delta_sum +  (value - avg) *  (value - avg) 
            
        variance = delta_sum / value_list_len
        
        #standard deviation        
        s = sqrt(variance)
        
        #median
        med = median(value_list)
        
        #1st quartile
        lower_half = []
        i = 0
        while (value_list[i] < med):
            lower_half.append(value_list[i])
            i = i +1
        
        q25 = median(lower_half)
            
        #3rd quartile
        upper_half = []
        j = value_list_len -1
        while (value_list[j] > med):
            upper_half.append(value_list[j])
            j = j - 1
            
        q75 = median(upper_half)
        
            
    return (total, avg, s, q25, med, q75)

def median(alist):
    median = 0
    list_len = len(alist)
    
    if (list_len <=0):
        return 0
    
    if (list_len % 2 ==0):
        value1 = alist[int(list_len / 2)]
        value2 = alist[int(list_len / 2) -1]
        median = (value1 + value2) / 2
    else:
        median = alist[int((list_len - 1) / 2)]
            
    return float(median)

print ("items: ",describe('items'))
print ("quantity: ", describe('quantity'))
print ("nic: " ,describe('nic'))
print ("act_cost: ",describe('act_cost'))

#2 Most Common Items
bnf_names = []

for script in scripts:
    if script['bnf_name'] not in bnf_names:
        bnf_names.append(script['bnf_name'])
        
print ("len bnf_names:", len(bnf_names))

groups = {name: [] for name in bnf_names}

for script in scripts:
    groups[script['bnf_name']].append(script)

    
def most_common_item():
    max_item =0
    max_bnf = "na"
    for name in bnf_names:
        script_list = groups[name]
        sum_items = 0
        for s in script_list:
            sum_items = sum_items + s['items']
        
        if (sum_items > max_item):
            max_item = sum_items
            max_bnf = name
            
    return [(max_bnf,max_item)]        
         
print ("most common bnf: ", most_common_item())   
                 
def group_by_field(data, fields):
    # we want to construct a dict of dict
    dicts = {}
    
    for field in fields:
        print ("building group for field:", field)
        
        temp_list = []
        #build a list of unique values for each field
        for d in data:           
            if d[field] not in temp_list:
                temp_list.append(d[field])
        
        #construct a dict base on the unique values of each field
        dict = {name : [] for name in temp_list}
    
        for d in data:
            dict[d[field]].append(d)
        
        #add the field dict to the general dict    
        dicts.update({field : dict})
        
    return dicts

#print ("group by field: ", group_by_field(scripts, ("bnf_name", "items")))    
totalDicts = group_by_field(scripts, ("bnf_name", "items"))
print ("len group dict", len(totalDicts["bnf_name"]))
print ("test group dict", (totalDicts["bnf_name"])["Omeprazole_Cap E/C 20mg"])
                        

