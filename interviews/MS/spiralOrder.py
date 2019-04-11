class Solution:
    """
    @param matrix: a matrix of m x n elements
    @return: an integer list
    """
    def spiralOrder(self, matrix):
        # write your code here
        
        if not matrix or not matrix[0]:
            
            return []
        
        up, down = 0, len(matrix) - 1 
        left, right = 0, len(matrix[0]) - 1 
        
        direction = 0 
        
        result = []
        
        while True:
            
            if direction == 0:
                
                for i in range(left, right + 1):
                
                    result.append(matrix[up][i])
                    
                up += 1 
                
            elif direction == 1:
                
                for i in range(up, down + 1):
                    
                    result.append(matrix[i][right])
                    
                right -= 1 
                
            elif direction == 2:
                
                for i in range(right, left - 1, -1):
                    
                    result.append(matrix[down][i])
                    
                down -= 1 
                
            elif direction == 3:
                
                for i in range(down, up - 1, -1):
                    
                    result.append(matrix[i][left])
                    
                left += 1 
                
            if left > right or up > down: 
                return result
            
            direction = (direction + 1) % 4 
            