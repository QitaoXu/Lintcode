from collections import deque 

DIRECTIONS = [(-1, 0), (0, -1), (1, 0), (0, 1)] 

# BFS
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

# DFS        
class Solution2:
    def maxAreaOfIsland(self, grid):
        
        if not grid or not grid[0]:
            return 0 
        
        m, n = len(grid), len(grid[0]) 
        
        max_area = 0 
        
        for i in range(m):
            for j in range(n):
                
                if grid[i][j] == 0:
                    continue 
                    
                max_area = max(max_area, self.dfs(grid, i, j, 1) ) 
                
        return max_area 
    
    def dfs(self, grid, x, y, count):
        
        grid[x][y] = 0 
        
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy 
            
            if not self.isValid(grid, nx, ny):
                continue 
                
            count = 1 + self.dfs(grid, nx, ny, count)
            
        return count 
    
    def isValid(self, grid, x, y):
        
        m, n = len(grid), len(grid[0]) 
        
        if x < 0 or x >= m or y < 0 or y >= n:
            return False 
        
        if grid[x][y] == 0:
            return False 
        
        return True         
        
# BFS without changing original grid       
class Solution3:
    def maxAreaOfIsland(self, grid):
        
        max_area = 0
        
        if not grid or not grid[0]:
            return max_area 
        
        m, n = len(grid), len(grid[0]) 
        visited = [[False for _ in range(n)] for _ in range(m)] 
        
        for i in range(m):
            for j in range(n):
                
                if grid[i][j] == 0:
                    continue 
                    
                if visited[i][j] == True:
                    continue 
                    
                island_area = self.bfs(grid, i, j, visited) 
                
                max_area = max(max_area, island_area) 
                
        return max_area 
    
    def bfs(self, grid, x, y, visited):
        
        queue = deque()
        seen = set() 
        
        queue.append((x, y))
        seen.add((x, y)) 
        visited[x][y] = True  
        
        while queue:
            
            size = len(queue) 
            
            for _ in range(size):
                
                cx, cy = queue.popleft()
                
                for dx, dy in DIRECTIONS:
                    
                    nx, ny = cx + dx, cy + dy 
                    
                    if not self.is_valid(grid, nx, ny, visited):
                        continue 
                        
                    queue.append((nx, ny))
                    seen.add((nx, ny))
                     
                    visited[nx][ny] = True 
                    
        return len(seen) 
    
    def is_valid(self, grid, x, y, visited):
        
        m, n = len(grid), len(grid[0]) 
        
        if x < 0 or x >= m or y < 0 or y >= n:
            return False 
        
        elif grid[x][y] == 0:
            return False 
        
        elif visited[x][y] == True:
            return False 
        
        else:
            return True      
        