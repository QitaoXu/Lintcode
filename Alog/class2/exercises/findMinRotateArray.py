class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        
        if not nums: 
            return -1 
        
        start, end = 0, len(nums) - 1 
        
        target = nums[-1]
        
        while start + 1 < end:
            
            mid = (start + end) // 2 
            
            if nums[mid] <= target:
                end = mid 
                
            else:
                start = mid 
                
        if nums[start] <= target:
            return nums[start] 
            
        elif nums[end] <= target:
            return nums[end]
        
            