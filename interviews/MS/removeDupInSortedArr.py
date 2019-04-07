class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """
    def removeDuplicates(self, nums):
        # write your code here
        
        size = 0
        
        for i in range(0, len(nums)):
            
            if nums[i] != nums[size]:
                
                nums[size + 1] = nums[i]
                
                size += 1 

        return size + 1  