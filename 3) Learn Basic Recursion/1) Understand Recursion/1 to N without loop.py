#!/usr/bin/env python
# coding: utf-8

# In[1]:


def generate_array(n, current=1, result=[]):
 
    if current > n:
        return result
    
    result.append(current)
    
    return generate_array(n, current + 1, result)

n = 5
output_array = generate_array(n)
print(output_array)


# In[ ]:




