class Solution:
    """
    @param matrix: the given matrix
    @return: the largest possible sum
    """
    def maxSubmatrix(self, matrix):
        # write your code here
        
        if not matrix or not matrix[0]:
            
            return 0
        
        n, m = len(matrix), len(matrix[0])
        
        max_sum = -sys.maxsize
        
        for top in range(n):
            
            arr = [0] * m 
            
            for down in range(top, n):
                
                min_sum = 0
                
                prefix_sum = 0 
                
                for col in range(m):
                    
                    arr[col] += matrix[down][col]
                    
                    prefix_sum += arr[col]
                    
                    max_sum = max(max_sum, prefix_sum - min_sum)
                    
                    min_sum = min(min_sum, prefix_sum)
                    
        return max_sum