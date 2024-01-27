#!/usr/bin/env python
# coding: utf-8

# In[6]:


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def delete_last_node(head):
 
    if not head or not head.next:
        return None
    
    
    current = head
    while current.next.next:
        current = current.next
    
    current.next = None
    
    return head

def print_linked_list(head):
    
    current = head
    while current:
        print(current.val, end=" ")
        current = current.next
    print()

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

head = delete_last_node(head)


print_linked_list(head)



# In[ ]:




