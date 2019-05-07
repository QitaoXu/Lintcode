class Solution:
    """
    @param matrix: a matrix of 0 an 1
    @return: an integer
    """
    def maxSquare2(self, matrix):
        # write your code here
        
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        
        
        l = [[0 for _ in range(n)] for _ in range(m)]
        u = [[0 for _ in range(n)] for _ in range(m)]
        f = [[0 for _ in range(n)] for _ in range(m)]
        
        length = 0 
        
        for i in range(m):
            for j in range(n):
                
                if matrix[i][j] == 0:
                    f[i][j] = 0 
                    
                    u[i][j], l[i][j] = 1, 1 
                    
                    if i > 0:
                        u[i][j] = u[i - 1][j] + 1 
                        
                    if j > 0:
                        l[i][j] = l[i][j - 1] + 1 
                        
                else:
                    
                    u[i][j], l[i][j] = 0, 0 
                    
                    if i > 0 and j > 0:
                        f[i][j] = min(f[i - 1][j - 1], u[i - 1][j], l[i][j - 1]) + 1 
                        
                    else:
                        f[i][j] = 1 
                        
                length = max(length, f[i][j])
                
        return length * length 