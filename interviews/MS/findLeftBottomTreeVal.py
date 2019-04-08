from collections import deque

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a root of tree
    @return: return a integer
    """
    def findBottomLeftValue(self, root):
        # write your code here
        
        left_bottom_node, _ = self.findBottomLeftValueHelper(root)
        
        return left_bottom_node.val 
        
    def findBottomLeftValueHelper(self, root):
        
        if root is None:
            
            return None, 0 
            
        l_left_bottom_node, l_height = self.findBottomLeftValueHelper(root.left)
        r_left_bottom_node, r_height = self.findBottomLeftValueHelper(root.right)
        
        if l_left_bottom_node is None and r_left_bottom_node is None: # leaf node 
            
            return root, 1 
            
        elif l_left_bottom_node and r_left_bottom_node is None:
            
            return l_left_bottom_node, l_height + 1 
            
        elif l_left_bottom_node is None and r_left_bottom_node:
            
            return r_left_bottom_node, r_height + 1 
            
        else:
            
            if r_height > l_height:
                
                return r_left_bottom_node, r_height + 1 
                
            else:
                
                return l_left_bottom_node, l_height + 1 