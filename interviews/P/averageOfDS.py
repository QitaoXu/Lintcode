from collections import deque
class MovingAverage:
    """
    @param: size: An integer
    """
    def __init__(self, size):
        # do intialization if necessary
        
        self.size = size 
        self.queue = deque()
        self.windowSum = 0

    """
    @param: val: An integer
    @return:  
    """
    def next(self, val):
        # write your code here
            
        self.queue.append(val)
        self.windowSum += val 
        
        if len(self.queue) > self.size:
            
            self.windowSum -= self.queue.popleft()
        
        return self.windowSum / len(self.queue)