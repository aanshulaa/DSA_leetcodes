#!/usr/bin/env python
# coding: utf-8

# In[2]:



def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


if __name__ == "__main__":
    a = 4
    b = 8
    print("The GCD of the two numbers is", gcd(a, b))


# In[ ]:




