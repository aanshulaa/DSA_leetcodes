#!/usr/bin/env python
# coding: utf-8

# In[1]:



def count_digits(n):
       count=0
       x=n
       while( x != 0 ):
               x//=10
               count+=1
       return count

n = 12345
print("Number of digits in ",n," is ",count_digits(n)) 

