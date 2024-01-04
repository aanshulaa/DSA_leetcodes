#!/usr/bin/env python
# coding: utf-8

# In[7]:



from math import sqrt

def isPrime(N):
    for i in range(2, int(sqrt(N))):
        if N % i == 0:
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




