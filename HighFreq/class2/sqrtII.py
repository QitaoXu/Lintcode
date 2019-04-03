class Solution:
    """
    @param x: a double
    @return: the square root of x
    """
    def sqrt(self, x):
        # write your code here
        
        accuracy = 1e-10 
        
        square = x 
        
        if x < 1: 
            
            square = 1 / square
            
        start, end = accuracy, square
        
        while start + accuracy < end:
            
            mid = (start + end) / 2 
            
            if mid ** 2 < square:
                
                start = mid 
                
            else:
                
                end = mid 
                
        if x < 1:
            
            start, end = 1 / end, 1 / start 
            
        if abs(start ** 2 - x) <= accuracy:
            
            return start 
            
        return end 
                
            
