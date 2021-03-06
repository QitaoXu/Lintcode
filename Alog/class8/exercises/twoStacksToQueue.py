class MyQueue:
    
    def __init__(self):
        # do intialization if necessary
        self.stack1 = []
        self.stack2 = []
    
    def stack2ToStack1(self):
        while self.stack2:
            self.stack1.append(self.stack2.pop())
    
    """
    @param: element: An integer
    @return: nothing
    """
    def push(self, element):
        # write your code here
        self.stack2.append(element)

    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        if not self.stack1:
            self.stack2ToStack1()
            
        return self.stack1.pop()

    """
    @return: An integer
    """
    def top(self):
        # write your code here
        if not self.stack1:
            self.stack2ToStack1()
            
        return self.stack1[-1]