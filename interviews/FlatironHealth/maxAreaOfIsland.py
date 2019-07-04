from collections import deque 

DIRECTIONS = [(-1, 0), (0, -1), (1, 0), (0, 1)] 

class Solution:
    """
    @param grid: a 2D array
    @return: the maximum area of an island in the given 2D array
    """
    def maxAreaOfIsland(self, grid):
        # Write your code here
        
        if not grid or not grid[0]:
            return 0 
        
        max_area = 0 
        
        m, n = len(grid), len(grid[0]) 
        
        for i in range(m):
            for j in range(n):
                
                if grid[i][j] == 0:
                    continue 
                
                island_area = self.bfs(grid, i, j) 
                
                max_area = max(max_area, island_area) 
        
        return max_area 
        
    def bfs(self, grid, x, y):
        
        queue = deque() 
        seen = set() 
        
        queue.append((x, y)) 
        seen.add((x, y)) 
        
        grid[x][y] = 0 
        
        while queue:
            
            size = len(queue) 
            
            for _ in range(size):
                
                cx, cy = queue.popleft() 
                
                for dx, dy in DIRECTIONS:
                    
                    nx, ny = cx + dx, cy + dy 
                    
                    if not self.is_valid(grid, nx, ny):
                        continue 
                    
                    if (nx, ny) in seen:
                        continue 
                    
                    queue.append((nx, ny)) 
                    seen.add((nx, ny))
                    grid[nx][ny] = 0 
                    
        return len(seen) 
        
    def is_valid(self, grid, x, y):
        
        m, n = len(grid), len(grid[0]) 
        
        if x < 0 or x >= m or y < 0 or y >= n:
            return False 
            
        if grid[x][y] == 0:
            return False 
            
        return True 
        
        
        
        
        
        
        
        