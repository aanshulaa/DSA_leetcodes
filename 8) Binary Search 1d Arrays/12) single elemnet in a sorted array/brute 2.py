#!/usr/bin/env python
# coding: utf-8

# In[3]:





        







def singleNonDuplicate(arr):
    n = len(arr)  
    ans = 0
    
    for i in range(n):
        ans = ans ^ arr[i]
    return ans

arr = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]
ans = singleNonDuplicate(arr)
print("The single element is:", ans)


# In[ ]:




