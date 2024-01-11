#!/usr/bin/env python
# coding: utf-8

# In[3]:


def find_index(arr, num):
    for i in range(len(arr)):
        if arr[i] == num:
            return i
    return -1

# Example usage:
n, num = map(int, input().split())
arr = list(map(int, input().split()))

result = find_index(arr, num)
print(result)


# In[ ]:




