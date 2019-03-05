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
        
        # start, end = source, destination 
        
        # if start == end:
        #     return 0 
            
        # queue = deque() 
        # distance = { (start.x, start.y) : 0}
        
        # queue.append( (start.x, start.y) )
        
        # while len(queue):
            
        #     size = len(queue)
            
        #     x, y = queue.popleft()
            
        #     if (x, y) == (end.x, end.y):
        #         return distance[(x, y)]
            
        #     for dx, dy in DIRECTIONS:
        #         next_x, next_y = x + dx, y + dy 
                
        #         if not self.is_valid(next_x, next_y, grid):
        #             continue 
        #         elif (next_x, next_y) in distance.keys():
        #             continue 
        #         else:
        #             queue.append((next_x, next_y))
        #             distance[(next_x, next_y)] = distance[(x,y)] + 1 
                    
        # return -1 
            
        
        # Bi BFS 
        start = source
        end = destination
        if start == end:
            return 0 
            
        startQueue, endQueue= deque(), deque() 
        startDistance, endDistance = {(start.x, start.y) : 0}, { (end.x, end.y) : 0}
        
        startQueue.append( (start.x, start.y) )
        endQueue.append( (end.x, end.y) )
        
        while len(startQueue) and len(endQueue):
            
            # startSize, endSize = len (startQueue), len(endQueue)
            
            # for _ in range(startSize):
                
            x, y = startQueue.popleft()
                
            for dx, dy in DIRECTIONS:
                next_x, next_y = x + dx, y + dy 
                    
                if not self.is_valid(next_x, next_y, grid):
                    continue 
                
                elif (next_x, next_y) in endDistance.keys():
                    return startDistance[(x,y)] + 1 + endDistance[(next_x, next_y)]
                    
                elif (next_x, next_y) in startDistance.keys():
                    continue 
                        
                else:
                    startQueue.append((next_x, next_y))
                    startDistance[(next_x, next_y)] = startDistance[(x,y)] + 1 

                        
            # for _ in range(endSize):
            x, y = endQueue.popleft()
                
            for dx, dy in DIRECTIONS:
                next_x, next_y = x + dx, y + dy 
                    
                if not self.is_valid(next_x, next_y, grid):
                    continue 
                
                elif (next_x, next_y) in startDistance.keys():
                    return endDistance[(x,y)] + 1 + startDistance[(next_x, next_y)]
                    
                elif (next_x, next_y) in endDistance.keys():
                    continue 
                
                else:
                    endQueue.append((next_x, next_y))
                    endDistance[(next_x, next_y)] = endDistance[(x,y)] + 1 
                        
        return -1 
    
    def is_valid(self, x, y, grid):
        
        row, col = len(grid), len(grid[0])
        
        if x < 0 or x >= row or y < 0 or y >= col:
            return False 
            
        if grid[x][y] == 1:
            return False 
            
        return True