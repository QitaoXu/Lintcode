# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def insertIntoBST(self, root, val):
        
        return self.insertInToBSTHelper(root, val) 
        
    def insertInToBSTHelper(self, root, val):
        
        if root is None:
            return TreeNode(val)
            
        if val < root.val:
            
            root.left = self.insertInToBSTHelper(root.left, val)
            
        else:
            
            root.right = self.insertInToBSTHelper(root.right, val)
            
        return root 