# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        
        if root is None:
            return None 
        
        if root.val < min(p.val, q.val):
            
            return self.lowestCommonAncestor(root.right, p, q)
        
        elif root.val > max(p.val, q.val):
            return self.lowestCommonAncestor(root.left, p, q)
        
        return root 