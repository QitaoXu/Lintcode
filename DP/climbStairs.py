class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        # write your code here
        if n == 0:
            
            return 0 
            
        if n <= 2:
            
            return n 
            
        result = [1, 2]
        
        for _ in range(3, n + 1):
            
            result.append(result[-1] + result[-2])
            
        return result[-1]