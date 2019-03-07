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
    @return: the value in the BST that is closest to the target
    """
    def __init__(self):
        self.closestDiff = sys.maxsize
        self.closestNode = None
        
    def closestValue(self, root, target):
        # write your code here
        if not root:
            return None 
        
        self.traverse(root, target)
        
        return self.closestNode.val
        
    def traverse(self, root, target):
        
        if root == None:
            return 
        
        self.traverse(root.left, target)
        
        diff = abs(root.val - target)
        
        if diff < self.closestDiff:
            self.closestDiff = diff 
            self.closestNode = root 
            
        self.traverse(root.right, target)