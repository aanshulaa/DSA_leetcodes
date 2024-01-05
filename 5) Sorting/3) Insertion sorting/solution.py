#!/usr/bin/env python
# coding: utf-8

# In[6]:


def recursive_insertion_sort(arr, N):
    if N <= 1:
        return
    
    # Recursively sort the first N-1 elements
    recursive_insertion_sort(arr, N - 1)
    
    # Insert the last element into the sorted part
    key = arr[N - 1]
    j = N - 2
    
    while j >= 0 and key < arr[j]:
        arr[j + 1] = arr[j]
        j -= 1
    
    arr[j + 1] = key

# Sample Input 1
N1 = 5
arr1 = [9, 3, 6, 2, 0]
recursive_insertion_sort(arr1, N1)
print(*arr1)  # Output: 0 2 3 6 9

# Sample Input 2
N2 = 4
arr2 = [4, 3, 2, 1]
recursive_insertion_sort(arr2, N2)
print(*arr2)  # Output: 1 2 3 4



# In[ ]:





# In[ ]:




