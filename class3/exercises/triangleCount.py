class Solution:
    """
    @param S: A list of integers
    @return: An integer
    """
    def triangleCount(self, S):
        # write your code here
        nums = S 
        result = 0
        
        if nums == None or len(nums) < 3:
            return result
            
        # start, end = 0, len(nums) - 1 
        nums.sort()
        
        for i in range(2, len(nums)):
            
            left, right = 0, i - 1 
            target = nums[i]
            
            while left < right:
                if nums[left] + nums[right] > target:
                    result += right - left
                    right -= 1 
                else:
                    left += 1 
                    
        return result
                    
                    
        
            