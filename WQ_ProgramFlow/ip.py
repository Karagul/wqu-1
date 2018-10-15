'''
Created on Oct 4, 2018

@author: ltran
'''
from WQ_Intro.HelloWorld import square
from math import sqrt, ceil

# Exercise 1: mersenne_number


def mersenne_number(p):
    i =1
    ans =1
    while i <= p:
        ans = ans*2
        i = i+1
        
    return ans-1

def is_prime(number):
    if number == 0 or number ==1:
        return False
    
    for factor in range(2, number):
        if number % factor == 0:
            return False

    return True

def get_primes(n_start, n_end):
    prime_list =[]
    for x in range(n_start,n_end+1):
        if is_prime(x):
            prime_list.append(x)
            
    return prime_list

def return_mersenne():
    prime_list = get_primes(3, 65)
    mersenne_list = []
    for x in prime_list:
        mersenne_list.append(mersenne_number(x))
        
    return mersenne_list

print ("mersenne list for p between 3 and 65: " , return_mersenne())
# Exercise 2: lucas_lehmer

def lucas_lehmer(p):
    lucas_lehmer_list = []
    
    nZero = 4
    i = p-2
    
    MERSENNEP = mersenne_number(p) #constant
    
    lucas_lehmer_list.append(nZero)
    
    index = 0
    while index < len(lucas_lehmer_list) and index < i:
        prev = lucas_lehmer_list[index]
        current = (square(prev) -2) % MERSENNEP
        lucas_lehmer_list.append(current)
        index = index +1
        
     
    return lucas_lehmer_list

print ("Lucas lehmer list for 5: ",lucas_lehmer(5))

# Exercise 3: mersenne_primes

def ll_prime(p):
    lucas_lehmer_list = lucas_lehmer(p)
    if lucas_lehmer_list[p-2] == 0:
        return True
    else:
        return False
    
def prime_test_results():
    p_prime_list = get_primes(3, 65)
    result_list = [] 
    for x in p_prime_list:
        if ll_prime(x):
             result_list.append((x,1))
        else:
             result_list.append((x,0))
    
    return result_list           
    
print ("Is 5^2 -1 a prime using ll_prime: ", ll_prime(5))
print ("For p from 3 to 65: ", prime_test_results())


# Exercise 4: Optimize is_prime

def is_prime_fast(n):
    
    if (n == 2):
        return True
        
    if (n>2 and n%2 ==0):
        return False
    
    m = ceil(sqrt(n))
    
    if (sqrt(n) == m):
        return False
    
    for factor in range(2, int(m+1)):
        if n % factor == 0:
            return False
    
    return True

def is_prime_fast_v2(number):
    
    if (number == 0 or number ==1):
        return False 
    if number % 2 == 0 and number > 2:
        return False
    else:
        for n in range (2, int(sqrt(number)+1)): 
            if number % n == 0:
                return False
    return number

print ("Check is_prime_fast: ", is_prime_fast(67867967))
# print ("Statement: ",is_prime(67867967))
def test():
    m = 0
    try:
        for n in range(10000):
            m = n
            assert is_prime(n) == is_prime_fast(n)
    except AssertionError as error:
        print (error)
        print ("The number causing error is: ",m )        
        
def get_primes_fast(n):
    prime_list = []
    for x in range(2,n+1):
        if (is_prime_fast(x)):
            prime_list.append(x)
            
    return prime_list        
        
print ("get primes fast 20", get_primes_fast(20))   

# Exercise 5: Sieve of Eratosthenes

def list_true(n):
    list_true = []
    for i in range(n+1):
        if (i==0 or i==1):
            list_true.append(False)
        else:    
            list_true.append(True)
        
    return list_true    

def mark_false(bool_list, p):

    list_len = len(bool_list)
    i = 2
    while (i*p < list_len):
        bool_list[i*p] = False
        i = i+1

    return bool_list


def find_next(bool_list,p):
    list_len = len(bool_list)
    i = p+1
    while (i < list_len):
        if (bool_list[i] == True):
            return i
        i = i+1
        
    return None

def prime_from_list(bool_list):
    true_list = []
    list_len = len(bool_list)
    i =0
    while (i < list_len):
        if (bool_list[i] == True):
            true_list.append(i)
        
        i = i+1    
            
    return true_list

def sieve(n):
    bool_list = list_true(n)
    p = 2
    while p is not None:
        bool_list = mark_false(bool_list, p)
        p = find_next(bool_list, p)
    
    return prime_from_list(bool_list)
    
list_t = list_true(5)
print ("List of truth: ", list_t)
print ("mark false: ",mark_false(list_t, 2))  
print ("find next: ", find_next(list_t, 2)) 
print ("prime from list: ", prime_from_list(list_t)) 
print ("sieve: ", sieve(200))

