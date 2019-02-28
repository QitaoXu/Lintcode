class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers(self, A):
        # write your code here
        
        if A == None or A == []:
            return 
        
        self.quickSort(A, 0, len(A) - 1)
        
        
    def quickSort(self, nums, start, end): 
        
        if start >= end:
            return 
        
        left, right = start, end 
        
        pivot = nums[(left + end) // 2]
        
        while left <= right:
            
            while left <= right and nums[left] < pivot:
                left += 1 
                
            while left <= right and nums[right] > pivot:
                right -= 1 
                
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1 
                right -= 1 
                
        self.quickSort(nums, start, right)
        self.quickSort(nums, left, end)