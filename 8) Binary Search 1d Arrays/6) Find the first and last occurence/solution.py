#!/usr/bin/env python
# coding: utf-8

# In[7]:


def find_first_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    first_occurrence = -1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            first_occurrence = mid
            right = mid - 1  
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return first_occurrence

def find_last_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    last_occurrence = -1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            last_occurrence = mid
            left = mid + 1  
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return last_occurrence

def find_first_and_last_occurrences(arr, target):
    first_occurrence = find_first_occurrence(arr, target)
    last_occurrence = find_last_occurrence(arr, target)

    return first_occurrence, last_occurrence

sorted_array = [1, 2, 2, 2, 4, 4, 4, 5, 6]
target_element = 4

first_occurrence, last_occurrence = find_first_and_last_occurrences(sorted_array, target_element)
print(f"First occurrence index of {target_element}: {first_occurrence}")
print(f"Last occurrence index of {target_element}: {last_occurrence}")



# In[ ]:




