#!/usr/bin/env python
# coding: utf-8

# In[3]:


class Node:
    def __init__(self, data1, next1=None):
        self.data = data1
        self.next = next1


def check_if_present(head, desired_element):
    temp = head

    while temp is not None:
      
        if temp.data == desired_element:
            return 1  

  
        temp = temp.next

    return 0 


if __name__ == "__main__":
   
    arr = [1, 2, 3]
    head = Node(arr[0])
    head.next = Node(arr[1])
    head.next.next = Node(arr[2])

    val = 3  
    print(check_if_present(head, val))


# In[ ]:




