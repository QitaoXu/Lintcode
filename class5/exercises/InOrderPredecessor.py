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
    @param p: the given node
    @return: the in-order predecessor of the given node in the BST
    """
    def inorderPredecessor(self, root, p):
        # write your code here
        
        stack = self.get_stack(root, p)
        
        self.move_lower(stack)
        
        if stack:
            return stack[-1]
            
        else:
            return None 
        
    def get_stack(self, root, p):
        stack = []
        
        while root:
            
            stack.append(root)
            
            if p.val < root.val:
                root = root.left
            
            elif p.val == root.val:
                break 
            
            else:
                root = root.right 
                
        return stack
        
    def move_lower(self, stack):
        node = stack[-1]
        
        if node.left == None:
            node = stack.pop() 
            
            while len(stack) > 0 and stack[-1].left == node:
                node = stack.pop()
                
        else:
            
            node = node.left 
            
            while node:
                stack.append(node)
                node = node.right
                
    
        
        
        