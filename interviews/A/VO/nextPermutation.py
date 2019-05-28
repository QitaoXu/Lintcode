class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if len(nums) <= 1:
            return 
        
        i = len(nums) - 1
        
        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1 
            
        if i != 0:
            
            j = len(nums) - 1 
            
            while nums[j] <= nums[i - 1]:
                j -= 1 
                
            nums[i - 1], nums[j] = nums[j], nums[i - 1]
            
        self.reverseNums(nums, i, len(nums) - 1)
        
    def reverseNums(self, nums, i, j):
        
        while i < j:
            
            nums[i], nums[j] = nums[j], nums[i]
            
            i += 1 
            j -= 1 
        