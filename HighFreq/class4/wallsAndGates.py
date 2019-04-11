from collections import deque

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def wallsAndGates(self, rooms):
        # write your code here
        
        queue = deque()
        distance = {}
        
        m = len(rooms)
        n = len(rooms[0]) 
        
        for i in range(m):
            
            for j in range(n):
                
                if rooms[i][j] == 0:
                    
                    queue.append((i, j))
                    distance[(i, j)] = 0 
                
        while queue:
            
            size = len(queue)
            
            for _ in range(size):
                
                x, y = queue.popleft()
                
                for dx, dy in DIRECTIONS:
                    
                    nx, ny = x + dx, y + dy 
                    
                    if not self.is_valid(nx, ny, rooms):
                        
                        continue 
                    
                    if (nx, ny) in distance:
                        
                        continue 
                    
                    queue.append((nx, ny))
                    
                    distance[(nx, ny)] = distance[(x, y)] + 1 
                    
                    rooms[nx][ny] = distance[(nx, ny)]
                
    def is_valid(self, x, y, rooms):
        
        m, n = len(rooms), len(rooms[0])
        
        if x < 0 or x >= m or y < 0 or y >= n:
            
            return False 
            
        if rooms[x][y] == -1:
            
            return False 
            
        return True 