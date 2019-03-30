from collections import deque 

DIRECTIONS = [
        (0, 1), (0, -1), (1, 0), (-1, 0)
    ]

class Solution:
    """
    @param grid: a 2D integer grid
    @return: an integer
    """
    
    def zombie(self, grid):
        # write your code here
        
        queue = deque() 
        
        distance = {} 
        
        
        n, m = len(grid), len(grid[0])
        
        walls = 0 
        
        for i in range(n):
            
            for j in range(m):
                
                if grid[i][j] == 1:
                    queue.append((i, j))
                    distance[(i, j)] = 0
                    
                if grid[i][j] == 2:
                    
                    walls += 1
        days = -1
        while queue:
            
            size = len(queue)
            
            days += 1 
            for _ in range(size):
                
                x, y = queue.popleft()
                
                for dx, dy in DIRECTIONS:
                    
                    nx, ny = x + dx, y + dy 
                    
                    if (nx, ny) in distance:
                        
                        continue 
                    
                    if not self.is_valid(nx, ny, grid):
                        
                        continue 
                    
                    grid[nx][ny] = 1
                    queue.append((nx, ny))
                    distance[(nx, ny)] = distance[(x, y)] + 1 
        
        if len(distance) == n * m - walls:
            
            return days
            
        return -1
        
    def is_valid(self, x, y, grid):
        
        row, col = len(grid), len(grid[0])
        
        if x < 0 or x >= row or y < 0 or y >= col:
            return False 
            
        if grid[x][y] == 2 or grid[x][y] == 1:
            return False 
            
        return True 