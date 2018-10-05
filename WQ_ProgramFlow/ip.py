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
    if number == 1:
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
    
    if (n>2 and n%2 ==0):
        return False
    
    for factor in range(2, int(sqrt(n))):
        if n % factor == 0:
            return False
    
    return True

print ("Check is_prime_fast: ", str(is_prime_fast(5)))