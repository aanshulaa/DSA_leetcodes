#!/usr/bin/env python
# coding: utf-8

# In[2]:


def sort_array(arr):
    low, mid, high = 0, 0, len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

# Sample Input 1
arr1 = [2, 2, 2, 2, 0, 0, 1, 0]
sort_array(arr1)
print(arr1)  # Output: [0, 0, 0, 1, 2, 2, 2, 2]

# Sample Input 2
arr2 = [1, 1, 1, 1, 1]
sort_array(arr2)
print(arr2)  # Output: [1, 1, 1, 1, 1]


# In[ ]:




