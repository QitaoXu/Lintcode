class Solution:
    """
    @param matrix: a boolean 2D matrix
    @return: an integer
    """
    def maximalRectangle(self, matrix):
        # write your code here
        if not matrix or not matrix[0]:
            
            return 0 
            
        heights = [0 for _ in range(len(matrix[0])) ]
        
        max_rectangle = 0
        
        for row in matrix:
            
            for index, num in enumerate(row):
                
                heights[index] = heights[index] + 1 if num else 0 
                
            max_rectangle = max(max_rectangle, self.find_max_rectangle(heights))
            
        return max_rectangle
        
    def find_max_rectangle(self, heights):
        
        if not heights:
            
            return 0 
            
        ans = 0 
        
        stack = []
        
        for i in range(len(heights) + 1):
            
            curt_height = heights[i] if i != len(heights) else 0 
            
            while stack and heights[stack[-1]] >= curt_height:
                
                h = heights[stack.pop()] 
                
                w = i - stack[-1] - 1 if stack else i 
                
                ans = max(ans, h * w)
                
            
            stack.append(i)
            
        return ans 