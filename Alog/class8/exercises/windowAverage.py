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
        if self.size == len(self.queue):
            
            self.windowSum -= self.queue.popleft()
            
        self.windowSum += val
        self.queue.append(val)
        
        return self.windowSum / len(self.queue)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param = obj.next(val)