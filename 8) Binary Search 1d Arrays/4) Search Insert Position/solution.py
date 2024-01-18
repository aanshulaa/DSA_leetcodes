#!/usr/bin/env python
# coding: utf-8

# In[1]:


def search_insert(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left


nums = [1, 3, 5, 6]
target = 5
result = search_insert(nums, target)
print("Index where", target, "should be inserted:", result)


# In[ ]:




