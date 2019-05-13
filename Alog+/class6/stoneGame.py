import sys
class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def stoneGame(self, A):
        # write your code here
        
        n = len(A)
        
        if n < 2:
            return 0 
            
        dp = [[0 for _ in range(n)] for _ in range(n)]
        
        range_sum = self.get_range_sum(A)
        
        for length in range(2, n + 1):
            for i in range(0, n - length + 1):
                
                j = i + length - 1 
                dp[i][j] = sys.maxsize 
                
                for k in range(i, j):
                    
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + range_sum[i][j])
                    
        return dp[0][n - 1]
        
    def get_range_sum(self, A):
        
        n = len(A) 
        range_sum = [[0 for _ in range(n)] for _ in range(n)]
        
        for i in range(0, n):
            range_sum[i][i] = A[i]
            
            for j in range(i + 1, n):
                
                range_sum[i][j] = range_sum[i][j - 1] + A[j]
                
        return range_sum
        
