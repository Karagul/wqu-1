'''
Created on Sep 27, 2018

@author: ltran

'''
from builtins import int
print ("Hello world from Long Tran")
# this is a comment in python

print ("1+1=", 1+1)

def square(x):
    return x**2

print (square(3))

def sayHello(name):
    print("Hello", name)
    
sayHello("Long") 

n=1
while (n < 10):
    print (n)
    n = n+1
    
def factorial(n):
    
    if not isinstance(n,int):
        raise TypeError('Expect point to be instance of int class. Got %s' % type(n))
    
    if (n < 0):
        return factorial(n * -1)
        
    if (n==0 or n ==1):
        return n
    
    return n*factorial(n-1)    

def factorial_mem(n, d):
    
    if n in d:
        return d[n]
    elif (n == 0 or n==1):
        ans = 1
    else:
        ans = n * factorial_mem(n-1, d)
    
    d[n] = ans
    
    return ans


print ("Factorial:", factorial(10))
print ("Factorial mem:", factorial(10))

