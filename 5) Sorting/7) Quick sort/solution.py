#!/usr/bin/env python
# coding: utf-8

# In[1]:


def quick_sort(arr, start, end):
    if start < end:
        # Partition the array and get the pivot index
        pivot_index = partition(arr, start, end)

        # Recursively sort the subarrays on both sides of the pivot
        quick_sort(arr, start, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, end)

def partition(arr, start, end):
    # Choosing the last element as the pivot
    pivot = arr[end]
    pivot_index = start - 1

    # Iterate through the array and rearrange elements based on the pivot
    for i in range(start, end):
        if arr[i] <= pivot:
            pivot_index += 1
            arr[i], arr[pivot_index] = arr[pivot_index], arr[i]

    # Swap the pivot element with the element at the pivot_index + 1
    arr[pivot_index + 1], arr[end] = arr[end], arr[pivot_index + 1]

    return pivot_index + 1

# Sample Input 1
arr1 = [2, 6, 8, 5, 4, 3]
start1, end1 = 0, len(arr1) - 1
quick_sort(arr1, start1, end1)
print(*arr1)  # Output: 2 3 4 5 6 8

# Sample Input 2
arr2 = [1, 2, 3, 5, 7]
start2, end2 = 0, len(arr2) - 1
quick_sort(arr2, start2, end2)
print(*arr2)  # Output: 1 2 3 5 7


# In[ ]:




