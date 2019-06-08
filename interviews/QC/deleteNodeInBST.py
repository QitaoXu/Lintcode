# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def successor(self, root):
        
        root = root.right 
        
        while root.left:
            
            root = root.left 
            
        return root.val 
    
    def predecessor(self, root):
        
        root = root.left 
        
        while root.right:
            
            root = root.right 
            
        return root.val 
    
    def deleteNode(self, root, key):
        
        if root is None:
            return None 
        
        if key < root.val:
            
            root.left = self.deleteNode(root.left, key)
            
        elif key > root.val:
            
            root.right = self.deleteNode(root.right, key)
            
        else:
            
            if root.left is None and root.right is None:
                root = None 
                
            elif root.right:
                
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
                
            else:
                
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)
                
        return root 