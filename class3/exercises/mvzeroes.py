class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        # write your code here
        
        if nums == None or len(nums) == 0:
            return 
        
        left, right = 0, 0 
        
        while right < len(nums):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1 
                
            right += 1 
        
        
        
        
        
        
        
        # if nums == None or len(nums) == 0:
        #     return 
        
        # left, right = 0, len(nums) - 1 
        
        # while left <= right:
            
        #     while left <= right and nums[left] != 0:
        #         left += 1 
            
        #     while left <= right and nums[right] == 0:
        #         right -= 1 
                
        #     if left <= right:
        #         nums[left], nums[right] = nums[right], nums[left]
        #         left += 1 
        #         right -= 1 