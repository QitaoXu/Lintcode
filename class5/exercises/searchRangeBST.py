"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    def searchRange(self, root, k1, k2):
        # write your code here
        
        if not root:
            return []
            
        nums = [] 
        
        self.traverse(root, nums)
        
        lower_index = self.find_lower_bound(nums, k1)
        upper_index = self.find_upper_bound(nums, k2)
        
        if lower_index < 0 or upper_index > len(nums) - 1:
            return []
        
        result = []
        
        for i in range(lower_index, upper_index + 1):
            result.append(nums[i])
            
        return result
        

    def traverse(self, root, result):
        
        if root == None:
            return 
        
        self.traverse(root.left, result)
        
        result.append(root.val)
        
        self.traverse(root.right, result)
        
        
    def find_lower_bound(self, nums, target):
        
        start, end = 0, len(nums) - 1 
        
        while start + 1 < end:
            
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
        
        
    def find_upper_bound(self, nums, target):
        
        start, end = 0, len(nums) - 1 
        
        while start + 1 < end:
            
            mid = (start + end) // 2 
            
            if nums[mid] <= target:
                
                start = mid 
                
            else:
                end = mid 
                
        if nums[end] <= target:
            return end 
            
        if nums[start] <= target:
            return start 
            
        return start - 1 
        
        
        