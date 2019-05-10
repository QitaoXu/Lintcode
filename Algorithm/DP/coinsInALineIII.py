class Solution:
    """
    @param values: a vector of integers
    @return: a boolean which equals to true if the first player will win
    """
    def firstWillWin(self, values):
        # write your code here
        
        if not values:
            return True 
            
        n = len(values)
            
        f = [ [0 for _ in range(n)] for _ in range(n) ] 
        
        for i in range(n):
            f[i][i] = values[i]
            
        for length in range(2, n + 1):
            
            for i in range(0, n - length + 1):
                
                j = i + length - 1 
                
                f[i][j] = max(values[i] - f[i + 1][j], values[j] - f[i][j - 1])
                
        return f[0][n - 1] >= 0 
            
        
