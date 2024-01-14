#!/usr/bin/env python
# coding: utf-8

# In[1]:


def is_possible_to_read_books(N, TARGET, BOOK):
    # Create a dictionary to store the frequency of pages
    page_frequency = {}

    # Iterate through the books
    for i in range(N):
        # Calculate the remaining pages needed to meet the target
        remaining_pages = TARGET - BOOK[i]

        # Check if the remaining pages are already encountered
        if remaining_pages in page_frequency and page_frequency[remaining_pages] > 0:
            return "YES"  # It's possible to find two books with the required pages

        # Update the frequency of the current book's pages
        page_frequency[BOOK[i]] = page_frequency.get(BOOK[i], 0) + 1

    return "NO"  # No two books found to meet the target

# Sample Input 1
N1, TARGET1, BOOK1 = 5, 5, [4, 1, 2, 3, 1]
print(is_possible_to_read_books(N1, TARGET1, BOOK1))  # Output: YES

# Sample Input 2
N2, TARGET2, BOOK2 = 2, 1, [1, 2]
print(is_possible_to_read_books(N2, TARGET2, BOOK2))  # Output: NO


# In[ ]:




