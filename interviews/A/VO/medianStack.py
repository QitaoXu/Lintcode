class LinkedNode:

    def __init__(self, val=None, next=None):
        self.val = val 
        self.next = next 

class MedianStack:

    def __init__(self):

        self.stack = []
    
    def push(self, item):
        self.stack.append(item)

    def pop(self):

        if not self.stack:
            return self.stack.pop()

        return None 

    def findMedian(self):

        size = len(self.stack)

        return self.stack[size // 2]