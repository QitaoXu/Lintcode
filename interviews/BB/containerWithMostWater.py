class Solution:
    """
    @param heights: a vector of integers
    @return: an integer
    """
    def maxArea(self, heights):
        # write your code here
        
        left, right = 0, len(heights) - 1 
        
        ans = 0 
        
        while left < right:
            
            if heights[left] < heights[right]:
                
                area = heights[left] * (right - left)
                
                left += 1 
                
            else:
                
                area = heights[right] * (right - left)
                
                right -= 1 
                
            ans = max(ans, area)
            
        return ans
