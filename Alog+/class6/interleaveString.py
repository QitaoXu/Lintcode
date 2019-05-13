class Solution:
    """
    @param s1: A string
    @param s2: A string
    @param s3: A string
    @return: Determine whether s3 is formed by interleaving of s1 and s2
    """
    def isInterleave(self, s1, s2, s3):
        # write your code here
        
        m, n, t = len(s1), len(s2), len(s3)
        
        if m + n != t:
            return False 
            
        f = [ [False for _ in range(n + 1)] for _ in range(m + 1)]
        
        f[0][0] = True  
        
        for i in range(1, m + 1):
            
            if s1[i - 1] == s3[i - 1] and f[i - 1][0] == True:
                f[i][0] = True 
                
        for j in range(1, n + 1):
            
            if s2[j - 1] == s3[j - 1] and f[0][j - 1] == True:
                f[0][j] = True 
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                
                if (f[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or \
                (f[i][j - 1] and s2[j - 1] == s3[i + j - 1]):
                    
                    f[i][j] = True 
                    
        return f[m][n]