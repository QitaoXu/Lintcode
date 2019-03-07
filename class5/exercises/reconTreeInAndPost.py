"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param inorder: A list of integers that inorder traversal of a tree
    @param postorder: A list of integers that postorder traversal of a tree
    @return: Root of a tree
    """
    def buildTree(self, inorder, postorder):
        # write your code here
        
        if inorder == None or len(inorder) == 0:
            return None 
        
        root = TreeNode(postorder[-1]) 
        
        rootPos = inorder.index(postorder[-1])
        
        root.left = self.buildTree(inorder[: rootPos], postorder[: rootPos])
        root.right = self.buildTree(inorder[rootPos + 1: ], postorder[rootPos : -1])
        
        return root 