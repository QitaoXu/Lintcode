class Solution:
    """
    @param nums: the given k sorted arrays
    @return: the median of the given k sorted arrays
    """
    def findMedian(self, nums):
        # write your code here
        
        if not nums:
            
            return 0.0
        
        n = sum([len(arr) for arr in nums]) 
        
        if n == 0:
            
            return 0.0 
            
        if n % 2 == 1:
            
            return self.find_kth(nums, n // 2 + 1) / 1.0
            
        else:
            
            return (self.find_kth(nums, n // 2) + self.find_kth(nums, n // 2 + 1)) / 2.0 
            
            
    
    def find_kth(self, nums, k):
        
        start, end = self.get_range(nums)
        
        while start + 1 < end:
            
            mid = (start + end) // 2 
            
            if self.get_less_or_equal(nums, mid) < k:
                
                start = mid 
                
            else:
                
                end = mid 
                
        if self.get_less_or_equal(nums, start) >= k:
            
            return start 
            
        return end 
            
        
    def get_range(self, nums):
        
        start = min( [arr[0] for arr in nums if len(arr)] )
        end = max( [ arr[-1] for arr in nums if len(arr) ] )
        
        return start, end 
        
    def get_less_or_equal(self, arrs, number):
        
        count = 0 
        
        for arr in arrs:
            
            count += self.get_less_or_equal_arr(arr, number)
            
        return count 
        
    def get_less_or_equal_arr(self, arr, number):
        
        if not arr:
            
            return 0
        
        start, end = 0, len(arr) - 1 
        
        
        while start + 1 < end:
            
            mid = (start + end) // 2 
            
            if arr[mid] <= number:
                
                start = mid 
                
            else:
                
                end = mid 
                
        if arr[start] > number:
            
            return start 
            
        if arr[end] > number:
            
            return end 
            
        return len(arr)