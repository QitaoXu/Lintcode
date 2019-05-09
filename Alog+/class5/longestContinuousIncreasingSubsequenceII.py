DIRECTION = [(0, 1), (0, -1), (1, 0), (-1, 0)]
class Solution:
    """
    @param matrix: A 2D-array of integers
    @return: an integer
    """
    def longestContinuousIncreasingSubsequence2(self, matrix):
        # write your code here
        if not matrix or not matrix[0]:
            return 0 
        
        m, n = len(matrix), len(matrix[0])
        
        dp = [ [-1 for _ in range(n) ] for _ in range(m) ]
        
        ans = 1 
        
        for i in range(m):
            for j in range(n):
                
                self.search(i, j, matrix, dp)
                
                ans = max(dp[i][j], ans)
                
        return ans 
        
    def search(self, x, y, matrix, dp):
        
        if dp[x][y] != -1:
            return 
        
        m, n = len(matrix), len(matrix[0])
        dp[x][y] = 1 
        
        for dx, dy in DIRECTION:
            nx, ny = x + dx, y + dy 
            
            if nx >= 0 and nx < m and ny >= 0 and ny < n:
                
                if matrix[nx][ny] > matrix[x][y]:
                    
                    self.search(nx, ny, matrix, dp)
                    dp[x][y] = max(dp[x][y],  dp[nx][ny] + 1)

class Solution2:
    """
    @param matrix: A 2D-array of integers
    @return: an integer
    """
    def longestContinuousIncreasingSubsequence2(self, matrix):
        # write your code here
        if not matrix or not matrix[0]:
            return 0 
        
        m, n = len(matrix), len(matrix[0])
        
        dp = [ [1 for _ in range(n) ] for _ in range(m) ]
        
        ans = 1
        
        memo = set()
        
        for i in range(m):
            for j in range(n):
                
                self.search(i, j, matrix, dp, memo)
                
                ans = max(dp[i][j], ans)
                
        return ans 
        
    def search(self, x, y, matrix, dp, memo):
        
        if (x, y) in memo:
            return dp[x][y]
        
        m, n = len(matrix), len(matrix[0])
        
        for dx, dy in DIRECTION:
            nx, ny = x + dx, y + dy 
            
            if nx >= 0 and nx < m and ny >= 0 and ny < n:
                
                if matrix[nx][ny] > matrix[x][y]:
                    
                    dp[x][y] = max(dp[x][y], self.search(nx, ny, matrix, dp, memo) + 1 )
                    
        memo.add((x, y))
                    
        return dp[x][y]