#!/usr/bin/env python
# coding: utf-8

# In[3]:


def selection_sort(arr, N):
    for i in range(N):
        min_index = i
        
        for j in range(i + 1, N):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Sample Input 1
N1 = 6
arr1 = [2, 13, 4, 1, 3, 6]
selection_sort(arr1, N1)
print(*arr1)  # Output: 1 2 3 4 6 13

# Sample Input 2
N2 = 5
arr2 = [9, 3, 6, 2, 0]
selection_sort(arr2, N2)
print(*arr2)  # Output: 0 2 3 6 9


# In[ ]:




