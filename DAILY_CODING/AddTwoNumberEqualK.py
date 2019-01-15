'''
Created on Jan 15, 2019
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

@author: ltran
'''
def addTwoNumberEqualK(num_list, k):
    list_len = len(num_list)