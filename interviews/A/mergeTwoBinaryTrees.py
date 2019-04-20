"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param t1: the root of the first tree
    @param t2: the root of the second tree
    @return: the new binary tree after merge
    """
    def mergeTrees(self, t1, t2):
        # Write your code here
        
        return self.mergeTreesHelper(t1, t2)
        
    def mergeTreesHelper(self, root1, root2):
        
        
        if not root1:
            
            return root2 
            
        if not root2:
            
            return root1 
            
        root = TreeNode(root1.val + root2.val)
        root.left = self.mergeTreesHelper(root1.left, root2.left)
        root.right = self.mergeTreesHelper(root1.right, root2.right)
        
        return root 