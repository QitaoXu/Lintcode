class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height:
            
            return 0
        
        left_max = [] 
        curt_max = -sys.maxsize 
        
        heights = height
        
        for height in heights:
            
            curt_max = max(curt_max, height)
            left_max.append(curt_max)
            
        right_max = [] 
        curt_max = -sys.maxsize 
        
        for height in reversed(heights):
            
            curt_max = max(curt_max, height)
            right_max.append(curt_max)
            
        right_max = right_max[::-1]
        
        water = 0
        
        for i in range(len(heights)):
            
            water += min(left_max[i], right_max[i]) - heights[i]
            
        return water
            
            