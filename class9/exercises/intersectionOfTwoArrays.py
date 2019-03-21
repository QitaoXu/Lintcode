class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """
    def intersection(self, nums1, nums2):
        # write your code here
        
        if not nums1 or not nums2:
            
            return []
        
        results_set = set()
        
        nums1.sort()
        # nums2.sort()
        
        for i in range(len(nums2)):
            
            if nums2[i] in results_set:
                
                continue 
            
            else:
                
                if self.binary_search(nums1, nums2[i]):
                    
                    results_set.add(nums2[i])
                    
        return list(results_set)
        
    def binary_search(self, nums, target):
        
        start, end = 0, len(nums) - 1 
        
        while start + 1 < end:
            
            mid = (start + end) // 2 
            
            if nums[mid] < target:
                
                start = mid 
                
            if nums[mid] > target:
                
                end = mid 
                
            if nums[mid] == target:
                
                return True 
                
        if nums[start] == target:
            
            return True 
            
        if nums[end] == target:
            
            return True 
            
        return False 