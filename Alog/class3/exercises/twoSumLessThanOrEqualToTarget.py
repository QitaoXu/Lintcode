class Solution:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    """
    def twoSum5(self, nums, target):
        # write your code here
        
        if nums == None or len(nums) == 0:
            return 0 
        
        left, right = 0, len(nums) - 1 
        
        count = 0 
        
        nums.sort()
        
        while left < right:
            
            if nums[left] + nums[right] <= target:
                count += right - left
                left += 1 
                
            else:
                right -= 1 
            
        return count    