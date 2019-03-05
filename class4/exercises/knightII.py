from collections import deque

DIRECTIONS = [
    (1, 2), (-1, 2),
    (2, 1), (-2, 1)
    ]


class Solution:
    """
    @param grid: a chessboard included 0 and 1
    @return: the shortest path
    """
    def shortestPath2(self, grid):
        # write your code here
        
        # BFS
        queue = deque()
        distance = {(0, 0) : 0}
        
        queue.append( (0, 0) )
        
        while len(queue):
            
            size = len(queue)
            
            for i in range(size):
                
                x, y = queue.popleft() 
                
                if (x, y) == ( len(grid) -1, len(grid[0]) - 1 ):
                    return distance[(x,y)]
                
                for dx, dy in DIRECTIONS:
                    next_x, next_y = x + dx, y + dy 
                    
                    if not self.is_valid(next_x, next_y, grid):
                        continue
                    
                    elif (next_x, next_y) in distance.keys():
                        continue
                    # elif (next_x, next_y) == ( len(grid) -1, len(grid[0]) - 1 ):
                    #     return distance[(x, y)] + 1 
                    else:
                        distance[(next_x, next_y)] = distance[(x, y)] + 1 
                        queue.append((next_x, next_y))
                        
        return -1     
        
        
    def is_valid(self, x, y, grid):
        
        row, col = len(grid), len(grid[0])
        
        if x < 0 or x >= row or y < 0 or y >= col:
            return False
            
        if grid[x][y] == 1:
            return False 
            
            
        return True 
        
        
