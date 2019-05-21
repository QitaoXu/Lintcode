from heapq import heappush, heappop

class DataStream:
    
    def __init__(self):
        
        self.maxheap = []
        self.minheap = []
        
    def median(self):
        
        return -self.maxheap[0]
        
    def add(self, num):
        
        if len(self.maxheap) <= len(self.minheap):
            
            heappush(self.maxheap, -num)
            
        else:
            
            heappush(self.minheap, num)
            
        if len(self.maxheap) == 0 or len(self.minheap) == 0:
            
            return 
        
        if -self.maxheap[0] > self.minheap[0]:
            
            heappush(self.maxheap, -heappop(self.minheap))
            heappush(self.minheap, -heappop(self.maxheap))
            
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