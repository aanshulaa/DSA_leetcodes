#!/usr/bin/env python
# coding: utf-8

# In[2]:



def lowerBound(arr: [int], n: int, x: int) -> int:
    for i in range(n):
        if arr[i] >= x:
           
            return i
    return n

if __name__ == "__main__":
    arr = [3, 5, 8, 15, 19]
    n = 5
    x = 9
    ind = lowerBound(arr, n, x)
    print("The lower bound is the index:", ind)



# In[ ]:




