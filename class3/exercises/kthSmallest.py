class Solution:
    """
    @param k: An integer
    @param nums: An integer array
    @return: kth smallest element
    """
    def kthSmallest(self, k, nums):
        # write your code here
        
        if nums == None or len(nums) == 0:
            return None 
            
        return self.quickSelect(nums, 0, len(nums) - 1, k)
            
        
    def quickSelect(self, nums, start, end, k):
        
        if start == end:
            return nums[start]
            
        i, j = start, end 
        pivot = nums[(start + end) // 2]
        
            
        while i <= j:
            while i <= j and nums[i] < pivot:
                i += 1 
                
            while i <= j and nums[j] > pivot:
                j -= 1 
                
            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1 
                j -= 1 
                
        if start + k - 1 <= j:
            return self.quickSelect(nums, start, j, k)
        
        if start + k - 1 >= i:
            return self.quickSelect(nums, i, end, k - (i - start))
            
        return nums[j + 1]
                