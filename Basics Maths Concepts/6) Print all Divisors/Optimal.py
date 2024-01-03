#!/usr/bin/env python
# coding: utf-8

# In[5]:



def printDivisorsOptimal(n):
    print("The Divisors of",n,"are:")
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            print(i, end=" ")
            if i != n/i:
                print(int(n/i), end=" ")
    print()
if __name__ == "__main__":
    printDivisorsOptimal(36)


# In[ ]:




