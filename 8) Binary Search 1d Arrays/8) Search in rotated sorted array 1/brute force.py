#!/usr/bin/env python
# coding: utf-8

# In[3]:


def search(arr, n, k):
    for i in range(n):
        if arr[i] == k:
            return i
    return -1

if __name__ == "__main__":
    arr = [7, 8, 9, 1, 2, 3, 4, 5, 6]
    n = 9
    k = 1
    ans = search(arr, n, k)
    if ans == -1:
        print("Target is not present.")
    else:
        print("The index is:", ans)

  


# In[ ]:




