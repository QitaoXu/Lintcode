from collections import deque

class Stack:
    """
    @param: x: An integer
    @return: nothing
    """
    
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()
        
    def moveItems(self):
        
        while len(self.queue1) != 1:
            item = self.queue1.popleft()
            self.queue2.append(item)
            
    def swapQueues(self):
        
        self.queue1, self.queue2 = self.queue2, self.queue1
        
    def push(self, x):
        # write your code here
        self.queue1.append(x)
        

    """
    @return: nothing
    """
    def pop(self):
        # write your code here
        self.moveItems()
        
        item = self.queue1.popleft()
        
        self.swapQueues()
        
        return item

    """
    @return: An integer
    """
    def top(self):
        # write your code here
        self.moveItems()
        
        item = self.queue1.popleft()
        
        self.queue2.append(item)
        
        self.swapQueues()
        
        return item

    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        # write your code here
        
        return len(self.queue1) == 0
