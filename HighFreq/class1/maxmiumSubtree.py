"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the maximum weight node
    """
    def findSubtree(self, root):
        # write your code here
        return self.findSubtreeHelper(root)[2]
        
    def findSubtreeHelper(self, root):
        
        if root is None:
            
            return 0, 0, None 
            
        left_max_sum, left_sum, left_root = self.findSubtreeHelper(root.left)
        right_max_sum, right_sum, right_root = self.findSubtreeHelper(root.right)
        
        curt_sum =  left_sum + right_sum + root.val
        max_sum = max(left_max_sum, right_max_sum, curt_sum)
        
        if max_sum == left_max_sum:
            
            max_root = left_root
            
        elif max_sum == right_max_sum:
            
            max_root = right_root
            
        else:
            
            max_root = root 
            
        return max_sum, curt_sum, max_root
        
        
