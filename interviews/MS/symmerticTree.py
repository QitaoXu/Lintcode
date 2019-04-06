"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: root of the given tree
    @return: whether it is a mirror of itself 
    """
    def isSymmetric(self, root):
        # Write your code here
        
        if not root:
            
            return True 
        
        return self.isSymmetricHelper(root.left, root.right)
        
    def isSymmetricHelper(self, left, right):
        
        if not left and not right:
            
            return True 
            
        if left and not right:
            
            return False 
            
        if not left and right:
            
            return False 
            
        if left.val != right.val:
            
            return False 
            
        return self.isSymmetricHelper(left.left, right.right) and \
                self.isSymmetricHelper(left.right, right.left)



class Solution2:
    """
    @param root: root of the given tree
    @return: whether it is a mirror of itself 
    """
    def isSymmetric(self, root):
        # Write your code here
        
        
        if not root:
            
            return True 
            
        stack = [] 
        
        stack.append(root.left)
        stack.append(root.right)
        
        while stack:
            
            l_node = stack.pop()
            r_node = stack.pop()
            
            if not l_node and not r_node:
                
                continue  
            
            if l_node and not r_node:
                
                return False 
                
            if not l_node and r_node:
                
                return False 
                
            if l_node.val != r_node.val:
                
                return False 
                
            stack.append(l_node.left)
            stack.append(r_node.right)
            
            stack.append(l_node.right)
            stack.append(r_node.left)
            
        return True 