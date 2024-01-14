#!/usr/bin/env python
# coding: utf-8

# In[3]:


def majority_element(n, arr):
    candidate = None
    count = 0

    # Find the potential majority candidate
    for num in arr:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1

    # Verify if the candidate is the majority element
    count = 0
    for num in arr:
        if num == candidate:
            count += 1

    if count > n // 2:
        return candidate
    else:
        return None

# Sample Input 1
n1, arr1 = 9, [2, 2, 1, 3, 1, 1, 3, 1, 1]
print(majority_element(n1, arr1))  # Output: 1

# Sample Input 2
n2, arr2 = 1, [4]
print(majority_element(n2, arr2))  # Output: 4

# Sample Input 3
n3, arr3 = 5, [-53, 75, 56, 56, 56]
print(majority_element(n3, arr3))  # Output: 56


# In[ ]:




