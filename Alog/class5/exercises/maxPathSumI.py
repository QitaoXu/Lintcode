"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxPathSum(self, root):
        # write your code here
        maxPath, _ = self.maxPathHelper(root)
        return maxPath
        
    def maxPathHelper(self, root):
        
        if root == None:
            return - sys.maxsize, 0
            
        left = self.maxPathHelper(root.left)
        right = self.maxPathHelper(root.right)
        
        maxPath = max(left[0], right[0], left[1] + right[1] + root.val)
        single = max(left[1] + root.val, right[1] + root.val, 0)
        
        return maxPath, single
