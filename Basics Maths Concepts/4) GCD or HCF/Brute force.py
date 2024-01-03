#!/usr/bin/env python
# coding: utf-8

# In[1]:



if __name__ == '__main__':
    num1 = 4
    num2 = 8
    ans = 1
    for i in range(1, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            ans = i
    print("The GCD of the two numbers is", ans)


# In[ ]:




