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
    @return: the root of the minimum subtree
    """
    def __init__(self):
        self.minSum = sys.maxsize
        self.minRoot = None
        
        
    def findSubtree(self, root):
        # write your code here
        if not root:
            return None 
            
        self.traverse(root)
        return self.minRoot
    
    # traverse    
    def traverse(self, root):
        
        if root == None:
            return 
        
        self.traverse(root.left)
        
        cur_subtree_sum = self.subTreeSum(root)
        
        if cur_subtree_sum < self.minSum:
            self.minSum = cur_subtree_sum
            self.minRoot = root 
            
        self.traverse(root.right)
        
        
    # divide conquer
    def subTreeSum(self, root):
        
        if root == None:
            return 0 
            
        leftSum = self.subTreeSum(root.left)
        rightSum = self.subTreeSum(root.right)
        
        return leftSum + rightSum + root.val