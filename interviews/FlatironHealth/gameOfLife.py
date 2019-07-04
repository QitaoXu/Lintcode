DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

class Solution:
    def gameOfLife(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        
        m, n = len(board), len(board[0])
        
        for i in range(m):
            for j in range(n):
                
                lives = self.getNeighborLives(board, i, j) 
                
                if board[i][j] == 0 and lives == 3:
                    board[i][j] = 2 
                    
                if board[i][j] == 1 and lives >= 2 and lives <= 3:
                    board[i][j] = 3 
                    
        for i in range(m):
            for j in range(n):
                board[i][j] = board[i][j] >> 1 
                
    def getNeighborLives(self, board, x, y):
        
        lives = 0 
        
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy 
            
            if not self.isValid(board, nx, ny):
                continue 
                
            if board[nx][ny] & 1 == 1:
                lives += 1 
                
        return lives 
    
    def isValid(self, board, x, y):
        
        m, n = len(board), len(board[0]) 
        
        if x < 0 or x >= m or y < 0 or y >= n:
            return False 
        
        return True 
    
    
    
    
            
            
            
            
            