from collections import deque 

DIRECTIONS = [
    [0, 1], [1, 0], [0, -1], [-1, 0]
    ]

class Solution:
    """
    @param grid: a 2D grid
    @return: An integer
    """
    def shortestDistance(self, grid):
        # write your code here
        
        if not grid or not grid[0]:
            
            return -1 
            
        m, n = len(grid), len(grid[0])
        
        house_to_empty_distance = [] 
        
        house_count = 0 
        
        for i in range(m):
            
            for j in  range(n):
                    
                if grid[i][j] == 1: # house
                    
                    self.bfs(grid, i, j, house_to_empty_distance, house_count)
                    
                    house_count += 1 
                    
        empty_reachable = set(house_to_empty_distance[0].keys())
        
        for i in range(1, house_count):
            
            empty_reachable = set(house_to_empty_distance[i].keys()) & empty_reachable
            
        empty_to_total_distance = {empty : 0 for empty in empty_reachable}
        
        for empty in empty_reachable:
            
            for count in range(house_count):
                
                empty_to_total_distance[empty] += house_to_empty_distance[count][empty]
                
        
        ans = sys.maxsize 
        
        for empty in empty_to_total_distance:
            
            ans = min(ans, empty_to_total_distance[empty])
            
        return ans if ans < sys.maxsize else -1 
        
        
    def bfs(self, grid, x, y, house_to_empty_distance, house_count):
        
        house_to_empty_distance.append(dict())
        
        house_to_empty_distance[house_count][(x, y)] = 0 
        
        queue = deque()
        
        queue.append((x, y))
        
        while queue:
            
            size = len(queue)
            
            for _ in range(size):
                
                cx, cy = queue.popleft()
                
                for dx, dy in DIRECTIONS:
                    
                    nx, ny = cx + dx, cy + dy 
                    
                    if not self.is_valid(grid, nx, ny):
                        
                        continue 
                    
                    if (nx, ny) in house_to_empty_distance[house_count]:
                        
                        continue 
                    
                    queue.append((nx, ny))
                    
                    house_to_empty_distance[house_count][(nx, ny)] = \
                        house_to_empty_distance[house_count][(cx, cy)] + 1 
        
        
        
    def is_valid(self, grid, x, y):
        
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            
            return False 
            
        if grid[x][y] == 2 or grid[x][y] == 1:
            
            return False 
            
        return True 