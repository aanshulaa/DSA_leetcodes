#!/usr/bin/env python
# coding: utf-8

# In[6]:



def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True




if __name__ == "__main__":
    n = 11
    ans = isPrime(n)
    if n != 1 and ans == True:
        print("Prime Number")
    else:
        print("Non Prime Number")


# In[ ]:




