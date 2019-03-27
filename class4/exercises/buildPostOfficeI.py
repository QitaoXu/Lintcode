HOUSE = 1 
EMPTY = 0

class Solution:
    """
    @param grid: a 2D grid
    @return: An integer
    """
    
    def shortestDistance(self, grid):
        # write your code here
        
        if not grid or not grid[0]:
            
            return -1 
            
        row_count = [0] * len(grid)
        
        col_count = [0] * len(grid[0])
        
        for i in range(len(grid)):
            
            for j in range(len(grid[0])):
                
                if grid[i][j] == HOUSE:
                    
                    row_count[i] += 1 
                    
                    col_count[j] += 1 
                    
        row_distance = [0] * len(grid)
        
        col_distance = [0] * len(grid[0])

        self.get_distance(len(grid), row_count, row_distance)
        self.get_distance(len(grid[0]), col_count, col_distance)
            
        result = sys.maxsize
            
        for i in range(len(grid)):
            
            for j in range(len(grid[0])):
                
                if grid[i][j] == EMPTY:
                    
                    result = min(result, row_distance[i] + col_distance[j])
                    
        return result
                
                
            
    def get_distance(self, size, count, distance):
        
        for i in range(size):
            
            for j in range(size):
                
                distance[i] += count[j] * abs(j - i)