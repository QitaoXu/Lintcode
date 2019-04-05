class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        # write your code here
        
        dp = [[0] * (n) for _ in range(m)]
        # dp = [[0] * (n + 1) for i in range(m + 1)]
        # dp[0][0] = 1
        
        for i in range(0, m):
            
            for j in range(0, n):
                
                if i == 0 or j == 0:
                    
                    dp[i][j] = 1 
                    
                else:
                    
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                
        return dp[m - 1][n - 1]