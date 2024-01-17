#!/usr/bin/env python
# coding: utf-8

# In[2]:



def upperBound(arr: [int], x: int, n: int) -> int:
    for i in range(n):
        if arr[i] > x:
        
            return i
    return n

if __name__ == "__main__":
    arr = [3, 5, 8, 9, 15, 19]
    n = 6
    x = 9
    ind = upperBound(arr, x, n)
    print("The upper bound is the index:", ind)


# In[ ]:




