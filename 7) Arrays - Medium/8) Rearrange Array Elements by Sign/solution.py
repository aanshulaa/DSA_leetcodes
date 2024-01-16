#!/usr/bin/env python
# coding: utf-8

# In[1]:


def rearrange_elements(arr, N):
    # Separate positive and negative elements
    positive_elements = [num for num in arr if num > 0]
    negative_elements = [num for num in arr if num < 0]

    # Initialize the result array
    result = []

    # Merge positive and negative elements alternatively
    for i in range(min(len(positive_elements), len(negative_elements))):
        result.append(positive_elements[i])
        result.append(negative_elements[i])

    # Append remaining positive or negative elements, if any
    result.extend(positive_elements[len(negative_elements):])
    result.extend(negative_elements[len(positive_elements):])

    return result

# Example 1
arr1 = [1, 2, -4, -5]
N1 = 4
output1 = rearrange_elements(arr1, N1)
print(output1)  # Output: [1, -4, 2, -5]

# Example 2
arr2 = [1, 2, -3, -1, -2, -3]
N2 = 6
output2 = rearrange_elements(arr2, N2)
print(output2)  # Output: [1, -3, 2, -1, 3, -2]


# In[ ]:




