class Solution:
    """
    @param: matrix: an integer matrix
    @return: the coordinate of the left-up and right-down number
    """
    def submatrixSum(self, matrix):
        # write your code here
        
        
        if not matrix or not matrix[0]:
            
            return None 
        
        n, m = len(matrix), len(matrix[0])
        
        for top in range(n):
            
            arr = [0] * m
            
            for down in range(top, n):
                
                prefix_sum_to_col = { 0 : -1 }
                prefix_sum = 0 
                
                for col in range(m):
                    
                    arr[col] += matrix[down][col]
                    
                    prefix_sum += arr[col]
                    
                    if prefix_sum in prefix_sum_to_col:
                        
                        return [ (top, prefix_sum_to_col[prefix_sum] + 1), (down, col)]
                        
                    prefix_sum_to_col[prefix_sum] = col 
                    
        return None 
                