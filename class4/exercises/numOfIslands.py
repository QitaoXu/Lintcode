from collections import deque 

DIRECTIONS = [
    (0, 1), (1, 0), (-1, 0), (0, -1)
    ]

class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        # write your code here
        isIslands = 0   
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    self.bfs(i, j, grid)
                    isIslands += 1 
                    
        return isIslands
        
        
    def bfs(self, x, y, grid):
        
        grid[x][y] = 0
            
        queue = deque()
        seen = set()
        queue.append((x, y))
        seen.add((x, y))
        
        while len(queue):
            
            x, y = queue.popleft() 
            
            for dx, dy in DIRECTIONS:
                next_x, next_y = x + dx, y + dy 
                
                if not self.is_valid(next_x, next_y, grid):
                    continue 
                if (next_x, next_y) in seen:
                    continue 
                
                queue.append((next_x, next_y))
                seen.add((next_x, next_y))
                grid[next_x][next_y] = 0
        
        
        
    def is_valid(self, x, y, grid):
        
        row, col = len(grid), len(grid[0])
        
        if x < 0 or x >= row or y < 0 or y >= col:
            return False 
        
        if grid[x][y] == 0:
            return False 
            
        return True 
        
        
