class Solution:
    """
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code here
        
        x = len(obstacleGrid)
        y = len(obstacleGrid[0])
        
        dp = [[0] * y for _ in range(x)]
        
        
        for i in range(x):
            
            if obstacleGrid[i][0] != 1:
            
                dp[i][0] = 1 
                
            else:
                
                break
            
        for j in range(y):
            
            if obstacleGrid[0][j] != 1:
            
                dp[0][j] = 1 
                
            else:
                
                break
            
        for i in range(1, x):
            
            for j in range(1, y):
                
                if obstacleGrid[i][j] == 1:
                    
                    dp[i][j] = 0 
                    
                else:
                    
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                    
        return dp[-1][-1]
                    
