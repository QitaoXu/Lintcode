class BinaryIndexTree:
    
    def __init__(self, matrix):
        
        self.n = len(matrix)
        self.m = len(matrix[0])
        
        self.arr = [[0] * self.m for _ in range(self.n)]
        self.blt = [[0] * (self.m + 1) for _ in range(self.n + 1)]
        
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
                
                self.blt[i][j] += delta
                
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
                
                ans += self.blt[i][j]
                
                j -= self.lowbit(j)
                
            i -= self.lowbit(i)
            
        return ans 


class NumMatrix:
    """
    @param: matrix: a 2D matrix
    """
    def __init__(self, matrix):
        # do intialization if necessary
        self.bit = BinaryIndexTree(matrix)

    """
    @param: row1: An integer
    @param: col1: An integer
    @param: row2: An integer
    @param: col2: An integer
    @return: An integer
    """
    def sumRegion(self, row1, col1, row2, col2):
        # write your code here
        
        return ( self.bit.prefix_sum(row2, col2) -
               self.bit.prefix_sum(row2, col1 - 1) -
               self.bit.prefix_sum(row1 - 1, col2) +
               self.bit.prefix_sum(row1 - 1, col1 - 1) )

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)