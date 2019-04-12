"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @return: collect and remove all leaves
    """
    def __init__(self):
        
        self.leaves = []
    
    
    def findLeaves(self, root):
        # write your code here
        
        self.helper(root)
        
        return self.leaves 
        
    def helper(self, root):
        
        if root is None:
            
            return 0 
            
        left_height = self.helper(root.left)
        right_height = self.helper(root.right)
        
        height = max(left_height, right_height) + 1 
        
        if height > len(self.leaves):
            
            self.leaves.append([])
            
        self.leaves[height - 1].append(root.val)
        
        return height 