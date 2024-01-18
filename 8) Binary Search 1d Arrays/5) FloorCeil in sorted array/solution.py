#!/usr/bin/env python
# coding: utf-8

# In[6]:


def floor_and_ceiling(arr, target):
    n = len(arr)

    floor_index = -1
    ceil_index = -1

    
    left, right = 0, n - 1
    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid, mid  
        elif arr[mid] < target:
            floor_index = mid
            left = mid + 1
        else:
            ceil_index = mid
            right = mid - 1

    return floor_index, ceil_index

sorted_array = [1, 2, 8, 10, 10, 12, 19]
target_element = 5

floor_idx, ceil_idx = floor_and_ceiling(sorted_array, target_element)
print(f"Floor index of {target_element}: {floor_idx}")
print(f"Ceiling index of {target_element}: {ceil_idx}")


# In[ ]:




