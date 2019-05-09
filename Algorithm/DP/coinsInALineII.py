class Solution:
    """
    @param values: a vector of integers
    @return: a boolean which equals to true if the first player will win
    """
    def firstWillWin(self, values):
        # write your code here
        
        n = len(values)
        
        f = [0 for _ in range(n + 1)]
        
        for i in range(n - 1, -1, -1):
            
            f[i] = values[i] - f[i + 1]
            
            if i < n - 1:
                f[i] = max(f[i], values[i] + values[i + 1] - f[i + 2])
        
        return f[0] >= 0 