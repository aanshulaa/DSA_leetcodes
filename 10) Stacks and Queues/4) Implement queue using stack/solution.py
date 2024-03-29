#!/usr/bin/env python
# coding: utf-8

# In[3]:


from queue import LifoQueue

class Queue:
    def __init__(self):
        self.input = LifoQueue()
        self.output = LifoQueue()


    def push(self, data: int) -> None:
        while not self.input.empty():
            self.output.put(self.input.get())
       
        print("The element pushed is", data)
        self.input.put(data)
     
        while not self.output.empty():
            self.input.put(self.output.get())


    def pop(self) -> int:
        if self.input.qsize() == 0:
            print("Stack is empty")
            exit(0)
        val = self.input.get()
        return val


    def Top(self) -> int:
        if self.input.qsize() == 0:
            print("Stack is empty")
            exit(0)
        return self.input.queue[-1]


    def size(self) -> int:
        return self.input.qsize()



if __name__ == "__main__":
    q = Queue()
    q.push(3)
    q.push(4)
    print("The element poped is", q.pop())
    q.push(5)
    print("The top of the queue is", q.Top())
    print("The size of the queue is", q.size())


# In[ ]:




