"""
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        # write your code here
        if not root:
            return None
            
        stack = self.get_stack(root, p)
        
        self.move_upper(stack)
        
        if len(stack) > 0:
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
        
        
        
    def move_upper(self, stack):
        
        node = stack[-1]
        
        if node.right == None:
            
            node = stack.pop()
            
            while len(stack) > 0 and stack[-1].right == node:
                node = stack.pop()
                
        else:
            node = node.right
            
            while node:
                
                stack.append(node)
                node = node.left