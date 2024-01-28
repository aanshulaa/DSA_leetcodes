#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

def length_of_linked_list(head):
    cnt = 0
    temp = head
    
        while temp is not None:
        temp = temp.next
        cnt += 1
  
    return cnt

def main():
    arr = [2, 5, 8, 7]

    head = Node(arr[0])
    head.next = Node(arr[1])
    head.next.next = Node(arr[2])
    head.next.next.next = Node(arr[3])

    print("Length of the linked list:", length_of_linked_list(head))
main()


# In[ ]:




