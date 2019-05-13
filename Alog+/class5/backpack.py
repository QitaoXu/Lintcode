class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        # write your code here
        
        n = len(A)
        
        f = [[False for _ in range(m + 1)] for _ in range(n + 1) ]
        
        f[0][0] = True 
        
        for i in range(1, n + 1):
            for w in range(0, m + 1):
                
                f[i][w] = f[i - 1][w]
                
                if w - A[i - 1] >= 0:
                    f[i][w] = f[i][w] or f[i - 1][w - A[i - 1]]
                    
    
        for w in range(m, -1, -1):
            
            if f[n][w]:
                return w
                
        return 0
                
