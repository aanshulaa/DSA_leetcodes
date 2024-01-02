#!/usr/bin/env python
# coding: utf-8

# In[1]:


def sum_of_even_odd_digits(n):
    # Initialize sum variables for even and odd digits
    sum_even = 0
    sum_odd = 0

    # Iterate through each digit in the number
    while n > 0:
        digit = n % 10

        # Check if the digit is even or odd
        if digit % 2 == 0:
            sum_even += digit
        else:
            sum_odd += digit

        # Remove the last digit from the number
        n //= 10

    return sum_even, sum_odd

# Input: Take an integer 'n' as input
n = int(input("Enter an integer (0<= n <= 10000): "))

# Calculate the sum of even and odd digits
even_sum, odd_sum = sum_of_even_odd_digits(n)

# Output: Print the sum of even and odd digits
print(f"Sum of even digits: {even_sum}")
print(f"Sum of odd digits: {odd_sum}")


# In[ ]:




