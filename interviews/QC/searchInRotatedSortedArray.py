class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        # write your code here
        
        if not A or target == None:
            return -1 
            
        nums = A 
        
        start, end = 0, len(nums) - 1 
        
        while start + 1 < end:
            
            mid = (start + end) // 2 
            
            if nums[mid] > nums[-1]:
                
                if nums[start] <= target <= nums[mid]:
                    
                    end = mid 
                    
                else:
                    
                    start = mid 
                    
            elif nums[mid] <= nums[-1]:
                
                if nums[mid] <= target <= nums[-1]:
                    
                    start = mid 
                    
                else:
                    
                    end = mid 
                    
        if nums[start] == target:
            
            return start 
            
        if nums[end] == target:
            
            return end 
            
        return -1 
            
    
