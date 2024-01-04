#!/usr/bin/env python
# coding: utf-8

# In[9]:


def fibonacci_generator(n):
    # Initializing the first two Fibonacci numbers
    a, b = 0, 1
    
    # Yield the first 'n' Fibonacci numbers using a loop
    for _ in range(n):
        yield a
        a, b = b, a + b

# Test cases
n1 = 5
fibonacci_sequence1 = list(fibonacci_generator(n1))
print(*fibonacci_sequence1)  # Output: 0 1 1 2 3

n2 = 3
fibonacci_sequence2 = list(fibonacci_generator(n2))
print(*fibonacci_sequence2)  # Output: 0 1 1


# In[ ]:




