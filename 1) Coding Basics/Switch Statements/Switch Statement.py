#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math

def calculate_area(ch, a):
    if ch == 1:
        # Calculate area of a circle with radius 'r'
        r = a[0]
        area = math.pi * r ** 2
        print(f"{area:.5f}")
    elif ch == 2:
        # Calculate area of a rectangle with length 'l' and breadth 'b'
        l, b = a
        area = l * b
        print(f"{area:.5f}")
    else:
        print("Invalid choice. Please choose 1 or 2.")

# Sample Input 1:
calculate_area(2, [3, 2])

# Sample Input 2:
calculate_area(1, [3])

