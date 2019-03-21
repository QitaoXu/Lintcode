class Solution:
    """
    @param arrs: the arrays
    @return: the number of the intersection of the arrays
    """
    def intersectionOfArrays(self, arrs):
        # write your code here
        
        if not arrs:
            return []
        
        return len(self.intersectionOfArraysHelper(0, len(arrs) - 1, arrs))
        
    def intersectionOfArraysHelper(self, start, end, arrs):
        
        if start >= end:
            
            return arrs[start]
            
        mid = (start + end) // 2 
            
        left = self.intersectionOfArraysHelper(start, mid, arrs)
        right = self.intersectionOfArraysHelper(mid + 1, end, arrs)
        
        return self.intersection(left, right)
        
    def intersection(self, A, B):
        
        hash_set = set()
        
        A.sort()
        
        for i in range(len(B)):
            
            if B[i] in hash_set:
                
                continue 
            
            else:
                
                if self.binary_search(A, B[i]):
                    
                    hash_set.add(B[i])
                    
        return list(hash_set)
        
    def binary_search(self, nums, target):
        
        if not nums:
            return False
        
        start, end = 0, len(nums) - 1 
        
        while start + 1 < end:
            
            mid = (start + end) // 2 
            
            if nums[mid] < target:
                
                start = mid 
                
            elif nums[mid] == target:
                
                return True 
                
            else:
                
                end = mid 
                
        if nums[start] == target:
            
            return True 
            
        if nums[end] == target:
            
            return True 
            
        return False 