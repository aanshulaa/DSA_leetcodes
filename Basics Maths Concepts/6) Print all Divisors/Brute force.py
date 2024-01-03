#!/usr/bin/env python
# coding: utf-8

# In[4]:



def printDivisorsBruteForce(n):
    print("The Divisors of ",n," are:")
    for i in range(1,n+1):
        if n % i == 0:
            print(i,end=" ")
    print()
if __name__ == "__main__":
    printDivisorsBruteForce(36)


# In[ ]:




