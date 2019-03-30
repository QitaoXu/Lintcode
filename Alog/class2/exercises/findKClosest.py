class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        # write your code here
        results = []
        
        if not A or target == None:
            return results
        
        # start, end = 0, len(A) - 1 
        nums = A 
        
        right = self.find_upperCloset(nums, target)
        left = right - 1
        
        for i in range(k):
            if self.is_left_close(nums, left, right, target):
                results.append(nums[left])
                left -= 1 
                
            else:
                results.append(nums[right])
                right += 1 
                
        return results
        
    def find_upperCloset(self, nums, target):
        
        start, end = 0, len(nums) - 1 
        
        
        while ( start + 1) < end:
             
            mid = ( start + end ) // 2  
            
            if nums[mid] >= target:
                end = mid 
                
            else:
                start = mid 
                
        if nums[start] >= target:
            return start 
            
        if nums[end] >= target:
            return end 
            
        return end + 1 
        
    def is_left_close(self, nums, left, right, target):
        if left < 0:
            return False
            
        if right >= len(nums):
            return True 
            
        else:
            return target - nums[left] <= nums[right] - target