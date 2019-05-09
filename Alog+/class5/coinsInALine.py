class Solution:
    """
    @param n: An integer
    @return: A boolean which equals to true if the first player will win
    """
    def firstWillWin(self, n):
        # write your code here
        if n < 0:
            return False 
        
        dp = [False for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            
            if i == 1:
                dp[i] = True 
                
            else:
                dp[i] = dp[i - 1] == False or dp[i - 2] == False 
                
        return dp[n]