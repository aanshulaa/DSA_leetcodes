#!/usr/bin/env python
# coding: utf-8

# In[4]:


def bubble_sort(arr, N):
    for i in range(N):
        # Last i elements are already in place, so we don't need to check them
        for j in range(0, N-i-1):
            if arr[j] > arr[j+1]:
                # Swap if the element found is greater than the next element
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Sample Input 1
N1 = 7
arr1 = [2, 13, 4, 1, 3, 6, 28]
bubble_sort(arr1, N1)
print(*arr1)  # Output: 1 2 3 4 6 13 28

# Sample Input 2
N2 = 5
arr2 = [9, 3, 6, 2, 0]
bubble_sort(arr2, N2)
print(*arr2)  # Output: 0 2 3 6 9


# In[ ]:




