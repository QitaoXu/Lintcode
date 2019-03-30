class Solution:
    """
    @param nums: An integer array
    @return: nothing
    """
    def recoverRotatedSortedArray(self, nums):
        # write your code here
        if not nums:
            return 
        
        for index in range(0, len(nums) - 1):
            if nums[index] > nums[index + 1]:
                self.reverse(nums, 0, index)
                self.reverse(nums, index + 1, len(nums) - 1)
                self.reverse(nums, 0, len(nums) - 1)
                return

    

    def reverse(self, nums, start, end):

        while start < end:
            
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp 
            
            start += 1 
            end -= 1 

        return