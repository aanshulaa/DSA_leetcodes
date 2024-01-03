#!/usr/bin/env python
# coding: utf-8

# In[1]:


def dataTypes(data_type: str):
    data_type_sizes = {
        'Integer': 4,
        'Long': 8,
        'Float': 4,
        'Double': 8,
        'Character': 1
    }

    if data_type in data_type_sizes:
        print(data_type_sizes[data_type])
    else:
        print("Invalid data type")

# Sample Input 1:
dataTypes('Long')

# Sample Input 2:
dataTypes('Float')


# In[ ]:




