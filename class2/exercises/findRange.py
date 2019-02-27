class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        # write your code here
        
        if not A or target == None:
            return [-1, -1]
            
        nums = A
            
        left = self.find_first(nums, target)
        right = self.find_last(nums, target)
                
            
        return [left, right]
        
    
    # find fisrt number equal to target   
    def find_first(self, nums, target): 
        
        start, end = 0, len(nums) - 1
        
        while ( start + 1 ) < end: 
            
            mid = ( start + end ) // 2 
            
            if nums[mid] == target:
                end = mid 
                
            elif nums[mid] < target:
                start = mid 
            
            elif nums[mid] > target:
                end = mid 
                
        if nums[start] == target:
            return start 
            
        if nums[end] == target:
            return end 
            
        return -1
    
    # find last number equal to target    
    def find_last(self, nums, target):
        start, end = 0, len(nums) - 1 
        
        while ( start + 1 ) < end:
            
            mid = ( start + end ) // 2 
            
            if nums[mid] == target:
                start = mid 
                
            elif nums[mid] < target:
                start = mid 
                
            elif nums[mid] > target:
                end = mid 
                
        if nums[end] == target:
            return end 
            
        if nums[start] == target:
            return start
            
        return -1