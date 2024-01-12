#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def longest_subarray_with_sum(nums, n, k):
    # Initialize variables
    sum_index_map = {0: -1}
    cumulative_sum = 0
    max_length = 0

    # Iterate through the array
    for i in range(n):
        cumulative_sum += nums[i]

        # Check if cumulative_sum - k is present in the map
        if cumulative_sum - k in sum_index_map:
            max_length = max(max_length, i - sum_index_map[cumulative_sum - k])

        # If cumulative_sum is not in the map, add it with the current index
        if cumulative_sum not in sum_index_map:
            sum_index_map[cumulative_sum] = i

    return max_length

# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    # Read input for each test case
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))

    # Call the function and print the result
    result = longest_subarray_with_sum(nums, n, k)
    print(result)



# In[ ]:




