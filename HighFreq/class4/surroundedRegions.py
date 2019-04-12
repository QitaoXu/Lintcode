from collections import deque

DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

class Solution:
    """
    @param: board: board a 2D board containing 'X' and 'O'
    @return: nothing
    """
    def surroundedRegions(self, board):
        # write your code here
        
        if not board or not board[0]:
            
            return []
        
        m, n = len(board), len(board[0])
        
        for j in range(n):
            
            if board[0][j] == 'O':
                
                self.bfs(0, j, board)
                
            if board[m - 1][j] == 'O':
                
                self.bfs(m - 1, j, board)
                
        for i in range(m):
            
            if board[i][0] == 'O':
                
                self.bfs(i, 0, board)
                
            if board[i][n - 1] == 'O':
                
                self.bfs(i, n - 1, board)
                
                
        for i in range(m):
            
            for j in range(n):
                
                if board[i][j] == 'O':
                    
                    board[i][j] = 'X'
                        
                if board[i][j] == 'W':
                    
                    board[i][j] = 'O'
                    
                    
    def bfs(self, x, y, board):
        
        queue = deque()
        seen = set()
        
        queue.append((x, y))
        seen.add((x, y))
        
        board[x][y] = 'W'
        
        while queue:
            
            size = len(queue)
            
            for _ in range(size):
                
                cx, cy = queue.popleft()
                
                for dx, dy in DIRECTIONS:
                    
                    nx, ny = cx + dx, cy + dy 
                    
                    if not self.is_valid(nx, ny, board):
                        
                        continue 
                    
                    if (nx, ny) in seen:
                        
                        continue 
                    
                    queue.append((nx, ny))
                    seen.add((nx, ny))
                    
                    board[nx][ny] = 'W'
                    
                    
    def is_valid(self, x, y, board):
        
        m, n = len(board), len(board[0])
        
        if x < 0 or x >= m or y < 0 or y >= n:
            
            return False 
            
        if board[x][y] == 'X' or board[x][y] == 'W':
            
            return False 
            
        return True 