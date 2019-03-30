"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree
    @return: An integer
    """
    def minDepth(self, root):
        # write your code here
        
        if root is None:
            return 0 
            
        leftMinDepth = self.minDepth(root.left)
        rightMinDepth = self.minDepth(root.right)
        
        if leftMinDepth == 0:
            return rightMinDepth + 1 
            
        elif rightMinDepth == 0:
            return leftMinDepth + 1 
            
        return min(leftMinDepth, rightMinDepth) + 1