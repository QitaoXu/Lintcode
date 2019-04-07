from collections import deque 

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

class Solution:
    """
    @param matrix: the height matrix
    @param R: the row of (R,C)
    @param C: the columns of (R,C)
    @return: Whether the water can flow outside
    """
    def waterInjection(self, matrix, R, C):
        # Write your code here
        
        queue = deque()
        
        seen = set()
        
        queue.append((R, C))
        
        seen.add((R, C))
        
        ans = False 
        
        while queue:
            
            size = len(queue)
            
            for _ in range(size):
                
                x, y = queue.popleft()
                
                if x == 0 or x == len(matrix) - 1 or y == 0 or y == len(matrix[0]) - 1:
                    
                    ans = True 
                    
                    break
                
                for dx, dy in DIRECTIONS:
                    
                    nx, ny = x + dx, y + dy
                    
                    if (nx, ny) in seen:
                        
                        continue 
                    
                    if matrix[nx][ny] > matrix[x][y]:
                        
                        continue
                    
                    queue.append((nx, ny))
                    
                    seen.add((nx, ny))
                    
        if ans:
            
            return "YES"
            
        else:
            
            return "NO"