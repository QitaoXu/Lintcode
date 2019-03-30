import heapq

class DataStream:
    
    def __init__(self):
        
        self.maxheap = []
        self.minheap = [] 
        
    def median(self):
        
        return -self.maxheap[0]
        
    def add(self, value):
        
        if len(self.maxheap) <= len(self.minheap):
            
            heapq.heappush(self.maxheap, -value)
            
        else:
            
            heapq.heappush(self.minheap, value)
            
        if len(self.minheap) == 0 or len(self.maxheap) == 0:
            
            return 
        
        if -self.maxheap[0] > self.minheap[0]:
            
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))
            
            heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))
            
class Solution:
    """
    @param nums: A list of integers
    @return: the median of numbers
    """
    def medianII(self, nums):
        # write your code here
        
        ds = DataStream()
        
        medians = []
        
        for num in nums:
            
            ds.add(num)
            
            medians.append(ds.median())
        
        return medians