class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        # write your code here
        
        if len(nums) == 0:
            return 0 
            
        nums.sort() 
        
        result = 1 
        
        for i in range(1, len(nums)):
            
            if nums[i - 1] != nums[i]:
                nums[result] = nums[i]
                result += 1 
                
        return result