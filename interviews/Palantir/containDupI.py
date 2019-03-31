class Solution:
    """
    @param nums: the given array
    @return: if any value appears at least twice in the array
    """
    def containsDuplicate(self, nums):
        # Write your code here
        
        nums.sort()
        
        for i in range(0, len(nums) - 1):
            
            if nums[i] == nums[i + 1]:
                
                return True 
                
        return False 
