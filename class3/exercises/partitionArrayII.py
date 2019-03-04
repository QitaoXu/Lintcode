class Solution:
    """
    @param nums: an integer array
    @param low: An integer
    @param high: An integer
    @return: nothing
    """
    def partition2(self, nums, low, high):
        # write your code here
        
        if nums == None or len(nums) == 0:
            return None 
            
        left, index, right = 0, 0, len(nums) - 1 
        
        while index <= right:
            
            if nums[index] < low:
                nums[left], nums[index] = nums[index], nums[left]
                left += 1 
                index += 1 
                
            elif low <= nums[index] <= high:
                index += 1 
                
            elif nums[index] > high:
                nums[right], nums[index] = nums[index], nums[right]
                right -= 1 
                
        
                
            
            
            