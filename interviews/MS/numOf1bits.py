class Solution:
    """
    @param n: an unsigned integer
    @return: the number of â1' bits
    """
    def hammingWeight(self, n):
        # write your code here
        
        if n == 0:
            
            return 0 
            
        count = 0 
        
        while n > 0:
            
            if n % 2 == 1:
                
                count += 1 
                
            n = n // 2 
            
        return count 
