class Solution:
    """
    @param height: A list of integer
    @return: The area of largest rectangle in the histogram
    """
    def largestRectangleArea(self, height):
        # write your code here
        
        if not height:
            
            return 0 
            
        ans = 0 
        stack = [] 
        
        for i in range(len(height) + 1):
            
            curt = -1 if i == len(height) else height[i]
            
            while stack and height[stack[-1]] >= curt:
                
                h = height[stack.pop()]
                
                w = i - stack[-1] - 1 if stack else i 
                
                ans = max(ans, h * w)
                
            stack.append(i)
            
        return ans 
                