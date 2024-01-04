#!/usr/bin/env python
# coding: utf-8

# In[8]:


def is_palindrome(s):
    # Base case: an empty string or a string with one character is a palindrome
    if len(s) <= 1:
        return True
    
    # Check if the first and last characters are the same
    if s[0] == s[-1]:
        # Recursive call with the substring excluding the first and last characters
        return is_palindrome(s[1:-1])
    
    # If the first and last characters are not the same, it's not a palindrome
    return False

# Test cases
print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("abbba"))    # Output: True
print(is_palindrome("abcd"))     # Output: False


# In[ ]:




