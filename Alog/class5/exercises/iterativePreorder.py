"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    # Recursive 
    # def preorderTraversal(self, root):
    #     # write your code here
        
    #     result = [] 
        
    #     self.preorderTraversalHelper(root, result)
        
    #     return result
    
    
    # def preorderTraversalHelper(self, root, result):
        
    #     if root == None:
    #         return 
        
    #     result.append(root.val)
    #     self.preorderTraversalHelper(root.left, result)
    #     self.preorderTraversalHelper(root.right, result)
        
    # Iterative
    def preorderTraversal(self, root):
        # write your code here  
        stack = [] 
        preorder = [] 
        
        if not root:
            
            return preorder 
            
        stack.append(root)
        
        while len(stack) > 0:
            
            node = stack.pop() 
            
            preorder.append(node.val)
            
            if node.right:
                stack.append(node.right)
                
            if node.left:
                stack.append(node.left)
                
        return preorder
            