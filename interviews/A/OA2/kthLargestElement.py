class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kthLargestElement(self, n, nums):
        # write your code here
        
        if nums == None or len(nums) == 0:
            return None 
            
        return self.quickSelect(nums, 0, len(nums) - 1, n)
        
        
    def quickSelect(self, nums, start, end, k):
        
        if start >= end:
            return nums[start]
        
        left, right = start, end 
        
        pivot = nums[ (start + end) // 2]  
        
        while left <= right:
            
            while left <= right and nums[left] > pivot:
                left += 1 
                
            while left <= right and nums[right] < pivot:
                right -= 1 
                
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1 
                right -= 1 
                
        if start + k - 1 <= right:
            return self.quickSelect(nums, start, right, k)
            
        elif start + k - 1 >= left:
            return self.quickSelect(nums, left, end, k - (left - start))
            
        else:
            return nums[right + 1]
        
        

            