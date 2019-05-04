import sys
class Solution:
    """
    @param nums: an integer array
    @param target: An integer
    @return: the difference between the sum and the target
    """
    def twoSumClosest(self, nums, target):
        # write your code here
        
        
        if not nums:
            
            return None 
            
        diff = sys.maxsize
        
        nums.sort()
        
        left, right = 0, len(nums) - 1 
        
        while left < right:
            
            if nums[left] + nums[right] < target:
                
                diff = min(diff, target - nums[left] - nums[right])
                
                left += 1 
                
            elif nums[left] + nums[right] == target:
                
                return 0 
                
            else:
                
                diff = min(diff, nums[left] + nums[right] - target)
                
                right -= 1 
                
        return diff 
        
        
            