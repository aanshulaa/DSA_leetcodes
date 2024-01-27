#!/usr/bin/env python
# coding: utf-8

# In[4]:


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def array_to_linked_list(arr):
    if not arr:
        return None

   
    head = ListNode(arr[0])
    current = head

    
    for num in arr[1:]:
        current.next = ListNode(num)
        current = current.next

    return head

arr = [4, 2, 5, 1]
head = array_to_linked_list(arr)


current = head
while current:
    print(current.val, end=" ")
    current = current.next
print()


# In[ ]:




