from collections import deque 

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""
DIRECTIONS = [
    (1, 2), (1, -2), (-1, 2),
    (-1, -2), (2, 1), (2, -1),
    (-2, 1), (-2, -1)
    ]

class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """
    def shortestPath(self, grid, source, destination):
        # write your code here

        # BFS
        start, end = source, destination 
        
        queue = deque()
        
        distance = {(start.x, start.y) : 0}
        
        queue.append((start.x, start.y))
        
        while queue:
            
            x, y = queue.popleft()
            
            if (x, y) == (end.x, end.y):
                
                return distance[(x, y)]
            
            for dx, dy in DIRECTIONS:
                
                nx, ny = x + dx, y + dy 
                
                if not self.is_valid(grid, nx, ny):
                    
                    continue 
                
                if (nx, ny) in distance:
                    
                    continue 
                
                queue.append((nx, ny))
                distance[(nx, ny)] = distance[(x, y)] + 1 
                
        return -1
        
    def is_valid(self, grid, x, y):
        
        row, col = len(grid), len(grid[0])
        
        if x < 0 or x >= row or y < 0 or y >= col:
            
            return False 
            
        if grid[x][y] == 1:
            
            return False 
            
        return True 
        
            