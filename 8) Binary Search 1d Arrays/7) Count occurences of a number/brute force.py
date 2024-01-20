#!/usr/bin/env python
# coding: utf-8

# In[1]:


def count(arr: [int], n: int, x: int) -> int:
    cnt = 0
    for i in range(n):
        if arr[i] == x:
            cnt += 1
    return cnt

if __name__ == "__main__":
    arr = [2, 4, 6, 8, 8, 8, 11, 13]
    n = 8
    x = 8
    ans = count(arr, n, x)
    print("The number of occurrences is:", ans)


# In[ ]:




