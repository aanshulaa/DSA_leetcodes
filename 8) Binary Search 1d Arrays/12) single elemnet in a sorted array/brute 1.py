#!/usr/bin/env python
# coding: utf-8

# In[3]:







def singleNonDuplicate(arr):
    n = len(arr)  
    if n == 1:
        return arr[0]

    for i in range(n):
       
        if i == 0:
            if arr[i] != arr[i + 1]:
                return arr[i]
        
        elif i == n - 1:
            if arr[i] != arr[i - 1]:
                return arr[i]
        else:
            if arr[i] != arr[i - 1] and arr[i] != arr[i + 1]:
                return arr[i]

   
    return -1

arr = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]
ans = singleNonDuplicate(arr)
print("The single element is:", ans)


        






# In[ ]:




