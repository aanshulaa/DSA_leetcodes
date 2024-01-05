#!/usr/bin/env python
# coding: utf-8

# In[1]:


def find_frequency_elements(n, v):
    frequency_dict = {}
    
    # Count the frequency of each element
    for num in v:
        frequency_dict[num] = frequency_dict.get(num, 0) + 1
    
    # Find the element with the highest frequency
    max_freq_element = max(frequency_dict, key=frequency_dict.get)
    
    # Find the element with the lowest frequency
    min_freq_element = min(frequency_dict, key=frequency_dict.get)
    
    return [max_freq_element, min_freq_element]

# Sample Input 1
n1 = 6
v1 = [1, 2, 3, 1, 1, 4]
print(find_frequency_elements(n1, v1))  # Output: [1, 2]

# Sample Input 2
n2 = 6
v2 = [10, 10, 10, 3, 3, 3]
print(find_frequency_elements(n2, v2))  # Output: [3, 3]


# In[ ]:




