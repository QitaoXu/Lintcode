import sys
class Solution:
    """
    @param n: An integer
    @param times: an array of integers
    @return: an integer
    """
    def copyBooksII(self, n, times):
        # write your code here
        
        # If there is nobody to work, 
        # n books cannot be copied forever.
        if not times:
            
            return sys.maxsize 
        
        start, end = 1, min(times) * n 
        
        while start + 1 < end:
            
            mid = start + (end - start) // 2 
            
            if self.can_complete(n, times, mid):
                
                end = mid 
                
            else:
                
                start = mid 
                
        if self.can_complete(n, times, start):
            
            return start 
            
        return end 
    
    # Compute how many books can be copied at most within tl time    
    def can_complete(self, n, times, tl):
        
        num = 0 
        
        for time in times:
            
            num += tl // time 
            
        return num >= n 