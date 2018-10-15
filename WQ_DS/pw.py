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
        total = sum(value_list)
        
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
            
    return median

print ("items: ",describe('items'))
print ("quantity: ", describe('quantity'))
print ("nic: " ,describe('nic'))
print ("act_cost: ",describe('act_cost'))
