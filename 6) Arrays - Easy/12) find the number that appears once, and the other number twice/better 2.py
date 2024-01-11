#!/usr/bin/env python
# coding: utf-8

# In[7]:





def get_single_element(arr):
    # Size of the array:
    n = len(arr)

    # Declare the hashmap.
    # And hash the given array:
    hashmap = {}
    for num in arr:
        hashmap[num] = hashmap.get(num, 0) + 1

    # Find the single element and return the answer:
    for num, count in hashmap.items():
        if count == 1:
            return num

    # This line will never execute
    # if the array contains a single element.
    return -1


def main():
    arr = [4, 1, 2, 1, 2]
    ans = get_single_element(arr)
    print("The single element is:", ans)


if __name__ == "__main__":
    main()




# In[ ]:




