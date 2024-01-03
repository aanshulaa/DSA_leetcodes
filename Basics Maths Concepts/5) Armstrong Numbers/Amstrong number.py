#!/usr/bin/env python
# coding: utf-8

# In[3]:


def ArmstrongNumber(n):
    originalno = n
    count = 0
    temp = n
    while temp != 0:
        count += 1
        temp //= 10
    sumofpower = 0
    while n != 0:
        digit = n % 10
        sumofpower += pow(digit, count)
        n //= 10
    return sumofpower == originalno




if __name__ == "__main__":
    n1 = 153
    if ArmstrongNumber(n1):
        print("Yes, it is an Armstrong Number")
    else:
        print("No, it is not an Armstrong Number")


# In[ ]:




