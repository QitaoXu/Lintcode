from collections import deque 

DIRECTIONS = [(-1, 0), (0, -1), (0, 1), (1, 0)]

class Solution:
    """
    @param grid: a list of lists of integers
    @return: return an integer, denote the number of distinct islands
    """
    def numberofDistinctIslands(self, grid):
        # write your code here
        
        if not grid or not grid[0]:
            
            return 0 
            
        m, n = len(grid), len(grid[0])
        
        islands = set()
        
        for i in range(m):
            for j in range(n):
                
                if grid[i][j] == 1:
                    
                    island = self.bfs(grid, i, j)
                    
                    islands.add(self.getUnique(island))
                    
        return len(islands)
        
    def bfs(self, grid, x, y):
        
        queue = deque()
        seen = set()
        
        grid[x][y] = 0 
        queue.append((x, y))
        seen.add((x, y))
        
        while queue:
            
            size = len(queue)
            
            for _ in range(size):
                
                cx, cy = queue.popleft()
                
                for dx, dy in DIRECTIONS:
                    
                    nx, ny = cx + dx, cy + dy 
                    
                    if not self.isValid(grid, nx, ny):
                        continue 
                    
                    if (nx, ny) in seen:
                        continue 
                    
                    queue.append((nx, ny))
                    seen.add((nx, ny))
                    grid[nx][ny] = 0 
                    
        return list(seen)
        
    def isValid(self, grid, x, y):
        m, n = len(grid), len(grid[0])
        
        if x < 0 or x >= m or y < 0 or y >= n:
            return False 
            
        if grid[x][y] == 0:
            return False 
            
        return True 
        
    def getUnique(self, island):
        
        island = sorted(island, key = lambda point:(point[0], point[1]))
        
        dx, dy = island[0]
        string = ""
        
        for point in island:
            
            x, y = point[0] - dx, point[1] - dy 
            string = string + str(x) + " " + str(y) + " "
            
        return string 
            
        
                
                
                
                
                
                
                
                