#!/usr/bin/env python
# coding: utf-8

# In[2]:


def frequency_array(n, x, arr):
    frequency = [0] * n

    for num in arr:
        if num <= n:
            frequency[num - 1] += 1

    return frequency

# Sample Input 1
n1, x1 = 6, 4
arr1 = [1, 3, 4, 3, 4, 1]
print(frequency_array(n1, x1, arr1))  # Output: [2, 0, 2, 2, 0, 0]

# Sample Input 2
n2, x2 = 5, 5
arr2 = [1, 2, 3, 4, 5]
print(frequency_array(n2, x2, arr2))  # Output: [1, 1, 1, 1, 1]


# In[ ]:




