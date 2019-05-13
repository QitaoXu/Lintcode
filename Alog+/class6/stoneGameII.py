import sys 
class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def stoneGame2(self, A):
        # write your code here
        n = len(A)
        if n < 2:
            return 0 
        
        dp = [[sys.maxsize for _ in range(2 * n)] for _ in range(2 * n)]
        s = [0]
        
        for i in range(0, 2 * n):
            
            s.append(s[-1] + A[i % n])
            dp[i][i] = 0 
            
        ans = sys.maxsize
            
        for length in range(2, 2 * n + 1):
            for i in range(0, 2 * n - length + 1):
                
                j = i + length - 1 
                
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + s[j + 1] - s[i])
                    
                if j - i + 1 == n:
                    ans = min(ans, dp[i][j])
                    
        return ans 