#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

class TambolaGame:
    def __init__(self):
        # Initialize a list of numbers from 1 to 90
        self.remaining_numbers = list(range(1, 91))

    def generate_random_number(self):
        # Generate a random number from the remaining numbers
        if self.remaining_numbers:
            number = random.choice(self.remaining_numbers)
            self.remaining_numbers.remove(number)
            return number
        else:
            return None

# Example of using the TambolaGame class
if __name__ == "__main__":
    # Create a TambolaGame instance
    tambola_game = TambolaGame()

    # Generate and print 10 random numbers
    for _ in range(10):
        random_number = tambola_game.generate_random_number()
        if random_number is not None:
            print(f"Generated Number: {random_number}")
        else:
            print("All numbers have been drawn.")
            break


# In[ ]:




