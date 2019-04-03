class MinStack:
    
    def __init__(self):
        # do intialization if necessary
        self.stack = []
        self.minStack = [] 

    """
    @param: number: An integer
    @return: nothing
    """
    def push(self, number):
        # write your code here
        
        self.stack.append(number)
        
        if not self.minStack:
            
            self.minStack.append(number)
            
        else:
            
            self.minStack.append(min(number, self.minStack[-1]))
        
    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        
        res = self.stack[-1]
        
        self.stack.pop()
        self.minStack.pop()
        
        return res 

    """
    @return: An integer
    """
    def min(self):
        # write your code here
        return self.minStack[-1]