#!/usr/bin/env python
# coding: utf-8

# In[6]:


def rotate_array(arr, k):
    n = len(arr)
    k = k % n  # Adjust k to avoid unnecessary rotations

    # Reverse the first part of the array
    arr[:k] = reversed(arr[:k])

    # Reverse the second part of the array
    arr[k:] = reversed(arr[k:])

    # Reverse the entire array
    arr.reverse()

# Example usage:
arr1 = [7, 5, 2, 11, 2, 43, 1, 1]
rotate_array(arr1, 2)
print(arr1)  # Output: [2, 11, 2, 43, 1, 1, 7, 5]

arr2 = [5, 6, 7, 8]
rotate_array(arr2, 3)
print(arr2)  # Output: [8, 5, 6, 7]


# In[ ]:




