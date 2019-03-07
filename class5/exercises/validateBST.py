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
    @return: True if the binary tree is BST, or false
    """
    # Solution 1: Traversal
    # def __init__(self):
    #     self.lastNode = None 
    #     self.isValid = True 
    
    
    # def isValidBST(self, root):
    #     # write your code here
    #     self.inorderTraverse(root)
        
    #     return self.isValid
        
    # def inorderTraverse(self, root):
        
    #     if root == None:
    #         return 
        
    #     self.inorderTraverse(root.left)
        
    #     if self.lastNode != None and self.lastNode.val >= root.val:
            
    #         self.isValid = False 
            
    #         return 
        
    #     self.lastNode = root 
        
    #     self.inorderTraverse(root.right)
        
        
    
    # Solution 2 Divide Conquer   
    def isValidBST(self, root):
        # write your code here
        minNode, maxNode, isValid = self.divideConquer(root)
        
        return isValid
        
        
    def divideConquer(self, root):
        
        if root == None:
            return None, None, True 
            
            
        leftMinNode, leftMaxNode, leftValid = self.divideConquer(root.left)
        rightMinNode, rightMaxNode, rightValid = self.divideConquer(root.right)
        
        if not leftValid or not rightValid:
            return None, None, False 
            
        if leftMaxNode != None and leftMaxNode.val >= root.val:
            return None, None, False 
            
        if rightMinNode != None and rightMinNode.val <= root.val:
            return None, None, False 
            
        minNode = leftMinNode if leftMinNode != None else root 
        maxNode = rightMaxNode if rightMaxNode != None else root 
        
        return minNode, maxNode, True 
        
        
        
