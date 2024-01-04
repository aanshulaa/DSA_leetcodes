#!/usr/bin/env python
# coding: utf-8

# In[2]:


def print_coding_ninjas(n):

    if n == 0:
        return
    
    print("Coding Ninjas", end=" ")
    
    print_coding_ninjas(n - 1)

n = 4
print_coding_ninjas(n)


# In[ ]:




