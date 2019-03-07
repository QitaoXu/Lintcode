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
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        # write your code here
        
        maxDepth, balance = self.maxDepth(root)
        
        return balance
        
    def maxDepth(self, root):
        
        if root == None:
            return 0, True 
            
        leftDepth, leftBalance = self.maxDepth(root.left)
        rightDepth, rightBalnce = self.maxDepth(root.right)
        
        if leftBalance == False or rightBalnce == False:
            return -1, False 
            
        if abs(leftDepth - rightDepth) > 1:
            return -1, False 
            
        return max(leftDepth, rightDepth) + 1, True 
