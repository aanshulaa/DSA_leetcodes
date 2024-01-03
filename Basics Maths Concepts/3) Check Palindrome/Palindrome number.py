#!/usr/bin/env python
# coding: utf-8

# In[2]:


def reverse(X):
    Y = 0
    while X > 0:
        # Extract the last digit
        digit = X % 10
        # Appending last digit
        Y = Y * 10 + digit
        # Shrinking X by discarding the last digit
        X = X // 10
    return Y




if __name__ == "__main__":
    X = 121
    dummy = X
    Y = reverse(X)
    if dummy == Y:
        print("Palindrome Number")
    else:
        print("Not Palindrome Number") 


# In[ ]:




