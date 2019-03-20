class BinaryIndexTree(object):
    
    def __init__(self, matrix):
        
        self.n = len(matrix)
        self.m = len(matrix[0])
        
        self.arr = [[0] * self.m for _ in range(self.n)]
        self.bit = [[0] * (self.m + 1) for _ in range(self.n + 1)]
        
        for i in range(self.n):
            for j in range(self.m):
                self.update(i, j, matrix[i][j])
                
    def update(self, row, col, value):
        
        delta = value - self.arr[row][col]
        
        self.arr[row][col] = value 
        
        i = row + 1 
        
        while i <= self.n:
            
            j = col + 1 
            
            while j <= self.m:
                
                self.bit[i][j] += delta 
                
                j += self.lowbit(j)
                
            i += self.lowbit(i)
            
    def lowbit(self, idx):
        
        return idx & -idx
        
    def prefix_sum(self, row, col):
        
        ans = 0 
        
        i = row + 1 
        
        while i > 0:
            
            j = col + 1
            
            while j > 0:
                
                ans += self.bit[i][j]
                
                j -= self.lowbit(j)
                
            i -= self.lowbit(i)
        
        return ans     
            


class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        self.bit = BinaryIndexTree(matrix)
        

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        self.bit.update(row, col, val)
        self.matrix[row][col] = val
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return ( self.bit.prefix_sum(row2, col2) -
               self.bit.prefix_sum(row2, col1 - 1) -
               self.bit.prefix_sum(row1 - 1, col2) +
               self.bit.prefix_sum(row1 - 1, col1 - 1) )
               
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)