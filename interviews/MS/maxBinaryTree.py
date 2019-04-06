"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import sys 

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param nums: an array
    @return: the maximum tree
    """
    def constructMaximumBinaryTree(self, nums):
        # Write your code here
        
        return self.constructHelper(nums, 0, len(nums) - 1)
        
    def constructHelper(self, nums, start, end):
        
        if start > end:
            
            return None 
        
        max_val = -sys.maxsize 
        index = start
        
        for i in range(start, end + 1):
            
            if nums[i] >= max_val:
                
                max_val = nums[i]
                index = i
        
        root = TreeNode(max_val)
        
        root.left = self.constructHelper(nums, start, index - 1)
        root.right = self.constructHelper(nums, index + 1, end)
        
        return root 
        