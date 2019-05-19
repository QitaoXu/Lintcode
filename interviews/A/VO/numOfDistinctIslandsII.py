from collections import deque

DIRECTIONS = [
    (0, 1), (1, 0), (-1, 0), (0, -1)
]

TRANS = [
    (1, 1), (-1, 1), (-1, -1), (1, -1)
]

class Solution:
    """
    @param grid: the 2D grid
    @return: the number of distinct islands
    """
    def numDistinctIslands2(self, grid):
        # write your code here
        
        if not grid or not grid[0]:
            
            return 0 
            
        m, n = len(grid), len(grid[0])
        islands = set()
        
        for i in range(m):
            for j in range(n):
                
                if grid[i][j] == 1:
                    
                    # Solution 1: DFS to find all islands
                    island = [] 
                    # self.dfs(grid, i, j, island)
                    
                    # Solution 2: BFS to find all islands
                    island = self.bfs(grid, i, j)
                    
                    islands.add(self.getUnique(island))
                    
        return len(islands)
        
    def dfs(self, grid, x, y, island):
        
        # m, n = len(grid), len(grid[0])
        
        island.append((x, y))
        
        grid[x][y] = 0 
        
        for dx, dy in DIRECTIONS:
            
            nx, ny = x + dx, y + dy 
            
            if not self.is_valid(grid, nx, ny):
                
                continue 
            
            self.dfs(grid, nx, ny, island)
            
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
        
        return list(seen)
        
    def is_valid(self, grid, x, y):
        
        m, n = len(grid), len(grid[0])
        
        if x < 0 or x >= m or y < 0 or y >= n:
            return False 
            
        if grid[x][y] == 0:
            return False 
            
        return True 
    
    def getUnique(self, island):
        
        sameIslands = [] 
        
        for t0, t1 in TRANS:
            
            island1, island2 = [], [] 
            
            for x, y in island:
                
                island1.append((x * t0, y * t1))
                island2.append((y * t0, x * t1))
                
            sameIslands.append(self.getStr(island1))
            sameIslands.append(self.getStr(island2))
                
        sameIslands = sorted(sameIslands)
        
        return sameIslands[0]
        
    def getStr(self, island):
        
        island = sorted(island, key = lambda pos:(pos[0], pos[1]))
        dx, dy = island[0]
        string = ""
        
        for point in island:
            
            x, y = point[0] - dx, point[1] - dy 
            string = string + str(x) + " " + str(y) + " "
            
        return string