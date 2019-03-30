"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @param k: the given k
    @return: k values in the BST that are closest to the target
    """
    def closestKValues(self, root, target, k):
        # write your code here
        
        nums = [] 
        result = []
        
        self.traverse(root, nums)
        
        right = self.binarySearch(nums, target) 
        left = right - 1
        
        for _ in range(k):
            
            if self.is_left_close(nums, left, right, target):
                result.append(nums[left])
                left -= 1 
                
            else:
                result.append(nums[right])
                right += 1 
                
        return result 
        
        
    def traverse(self, root, result):
        
        if root == None:
            return 
        
        self.traverse(root.left, result)
        
        result.append(root.val)
        
        self.traverse(root.right, result)
        
        
    def binarySearch(self, nums, target):
        
        start, end = 0, len(nums) - 1
        
        while start + 1 < end:
            
            mid = (start + end) // 2 
            
            if nums[mid] >= target:
                end = mid 
                
            if nums[mid] < target:
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
            
        return target - nums[left] <= nums[right] - target
