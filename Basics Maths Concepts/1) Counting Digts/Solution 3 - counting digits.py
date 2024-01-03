#!/usr/bin/env python
# coding: utf-8

# In[3]:


import math

def count_digits(n):
    digits = math.floor(math.log10(n) + 1)
    return digits

n = 12345
print("Number of digits in", n, "is", count_digits(n))

