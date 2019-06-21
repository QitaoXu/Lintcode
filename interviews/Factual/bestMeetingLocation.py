class Solution:
    def minTotalDistance(self, grid):
        
        rows = self.get_rows(grid)
        cols = self.get_cols(grid) 
        
        row = rows[len(rows) // 2]
        col = cols[len(cols) // 2] 
        
        return self.minDistance1D(rows, row) + self.minDistance1D(cols, col) 
    
    def minDistance1D(self, points, orign):
        
        distance = 0 
        
        for point in points:
            
            distance += abs(point - orign) 
            
        return distance 
    
    def get_rows(self, grid):
        
        m, n = len(grid), len(grid[0]) 
        rows = [] 
        
        for i in range(m):
            for j in range(n):
                
                if grid[i][j] == 1:
                    rows.append(i)
                    
        return rows 
    
    def get_cols(self, grid):
        
        m, n = len(grid), len(grid[0]) 
        cols = []
        
        for j in range(n):
            for i in range(m):
                
                if grid[i][j] == 1:
                    cols.append(j) 
                    
        return cols 