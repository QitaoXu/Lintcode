class Solution:
    """
    @param: num: An integer
    @return: An integer
    """
    def countOnes(self, num):
        # write your code here
        
        total = 0
        
        for _ in range(32):
            
            total += num & 1 
            
            num = num >> 1 
            
        return total