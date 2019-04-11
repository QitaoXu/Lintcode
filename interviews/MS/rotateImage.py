class Solution:
    """
    @param matrix: a lists of integers
    @return: nothing
    """
    def rotate(self, matrix):
        # write your code here
        
        n = len(matrix)
        
        # transpose
        for i in range(n):
            
            for j in range(i, n):
                
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
                
        # reverse each row        
        for i in range(n):
            
            matrix[i].reverse()