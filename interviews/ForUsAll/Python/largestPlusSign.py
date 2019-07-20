class Solution:
    def orderOfLargestPlusSign(self, N, mines):
        
        banned = {tuple(mine) for mine in mines} 
        
        dp = [[0 for _ in range(N)] for _ in range(N)] 
        ans = 0 
        
        for r in range(N):
            
            count = 0 
            
            for c in range(N):
                
                count = 0 if (r, c) in banned else count + 1 
                dp[r][c] = count 
                
            count = 0 
            
            for c in range(N - 1, -1, -1):
                
                count = 0 if (r, c) in banned else count + 1
                dp[r][c] = min(dp[r][c], count) 
                
        for c in range(N):
            
            count = 0 
            
            for r in range(N):
                count = 0 if (r, c) in banned else count + 1
                dp[r][c] = min(dp[r][c], count) 
                
            count = 0 
            
            for r in range(N - 1, -1, -1):
                
                count = 0 if (r, c) in banned else count + 1
                dp[r][c] = min(dp[r][c], count) 
                
                ans = max(ans, dp[r][c])
                
        return ans 