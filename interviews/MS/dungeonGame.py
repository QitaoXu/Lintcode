class Solution:
    """
    @param dungeon: a 2D array
    @return: return a integer
    """
    def calculateMinimumHP(self, dungeon):
        # write your code here
        
        m, n = len(dungeon), len(dungeon[0])
        
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        dp[-1][-1] = max(1, 1 - dungeon[-1][-1])
        
        for j in range(n - 2, -1, -1):
            
            dp[m - 1][j] = max(dp[m - 1][j + 1] - dungeon[m - 1][j], 1)
            
        for i in range(m - 2, -1, -1):
            
            dp[i][n - 1] = max(dp[i + 1][n - 1] - dungeon[i][n - 1], 1)
            
        for i in range(m - 2, -1, -1):
            
            for j in range(n - 2, -1, -1):
                
                curr = min(dp[i + 1][j], dp[i][j + 1])
                
                dp[i][j] = max(curr - dungeon[i][j], 1)
                
        return dp[0][0]