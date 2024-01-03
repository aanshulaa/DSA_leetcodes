#!/usr/bin/env python
# coding: utf-8

# In[1]:


def find_fibonacci(n):
    
    if n == 1:
        return 1
    elif n == 2:
        return 1
    
    a, b = 1, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b
n = 6

result = find_fibonacci(n)
print(result)


# In[ ]:




