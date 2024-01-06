#!/usr/bin/env python
# coding: utf-8

# In[5]:


def merge_sort(arr, l, r):
    if l < r:
        mid = (l + r) // 2

        # Recursively sort the first and second halves
        merge_sort(arr, l, mid)
        merge_sort(arr, mid + 1, r)

        # Merge the sorted halves
        merge(arr, l, mid, r)

def merge(arr, l, mid, r):
    n1 = mid - l + 1
    n2 = r - mid

    # Create temporary arrays
    left_arr = arr[l:l + n1]
    right_arr = arr[mid + 1:mid + 1 + n2]

    i = j = 0
    k = l

    # Merge the temporary arrays back into arr[l..r]
    while i < n1 and j < n2:
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    # Copy the remaining elements of left_arr, if any
    while i < n1:
        arr[k] = left_arr[i]
        i += 1
        k += 1

    # Copy the remaining elements of right_arr, if any
    while j < n2:
        arr[k] = right_arr[j]
        j += 1
        k += 1

# Sample Input 1
N1 = 7
ARR1 = [2, 13, 4, 1, 3, 6, 28]
merge_sort(ARR1, 0, N1 - 1)
print(*ARR1)  # Output: 1 2 3 4 6 13 28

# Sample Input 2
N2 = 5
ARR2 = [9, 3, 6, 2, 0]
merge_sort(ARR2, 0, N2 - 1)
print(*ARR2)  # Output: 0 2 3 6 9


# In[ ]:




