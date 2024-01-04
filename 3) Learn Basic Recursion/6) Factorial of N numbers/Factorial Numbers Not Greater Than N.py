#!/usr/bin/env python
# coding: utf-8

# In[6]:


def generate_factorials(n):
    factorials = []
    current_factorial = 1
    i = 1

    while current_factorial <= n:
        factorials.append(current_factorial)
        i += 1
        current_factorial *= i

    return factorials

# Test cases
n1 = 7
print(generate_factorials(n1))  # Output: [1, 2, 6]

n2 = 2
print(generate_factorials(n2))  # Output: [1, 2]


# In[ ]:




