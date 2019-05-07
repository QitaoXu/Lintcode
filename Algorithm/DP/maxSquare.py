class Solution:
    """
    @param matrix: a matrix of 0 and 1
    @return: an integer
    """
    def maxSquare(self, matrix):
        # write your code here
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        
        ans = 0 
        
        res = [ [0 for _ in range(n)] for _ in range(m) ]
        
        for i in range(m):
            res[i][0] = matrix[i][0]
            ans = max(ans, res[i][0])
            
        for j in range(n):
            res[0][j] = matrix[0][j]
            ans = max(ans, res[0][j])
            
        for i in range(1, m):
            for j in range(1, n):
                
                if matrix[i][j] == 0:
                    
                    res[i][j] = 0 
                    
                else:
                    
                    res[i][j] = min(res[i - 1][j], res[i][j - 1], res[i - 1][j - 1]) + 1 
                    
                ans = max(ans, res[i][j])
                
        return ans * ans 
        
        
        
