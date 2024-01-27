#!/usr/bin/env python
# coding: utf-8

# In[5]:


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def insert_at_beginning(head, val):
   
    new_node = ListNode(val)
    
    new_node.next = head
    
    head = new_node
    
    return head

def print_linked_list(head):
    
    current = head
    while current:
        print(current.val, end=" ")
        current = current.next
    print()


head = ListNode(1)
head = insert_at_beginning(head, 2)
head = insert_at_beginning(head, 3)


print_linked_list(head)


# In[ ]:




