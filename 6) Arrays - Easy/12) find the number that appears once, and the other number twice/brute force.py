#!/usr/bin/env python
# coding: utf-8

# In[5]:





def getSingleElement(arr):
    # Size of the array:
    n = len(arr)

    # Run a loop for selecting elements:
    for i in range(n):
        num = arr[i]  # selected element
        cnt = 0

        # Find the occurrence using linear search:
        for j in range(n):
            if arr[j] == num:
                cnt += 1

        # If the occurrence is 1, return the number:
        if cnt == 1:
            return num

    # This line will never execute
    # if the array contains a single element.
    return -1


def main():
    arr = [4, 1, 2, 1, 2]
    ans = getSingleElement(arr)
    print("The single element is:", ans)


if __name__ == '__main__':
    main()



# In[ ]:




