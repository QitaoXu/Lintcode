"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """
    def longestConsecutive2(self, root):
        # write your code here
        
        max_len, _, _ = self.longestConsecutiveHelper(root)
        
        return max_len
            
    def longestConsecutiveHelper(self, root):
        
        if root == None:
            return 0, 0, 0 
            
        left_max_len, left_down, left_up = self.longestConsecutiveHelper(root.left)
        right_max_len, right_down, right_up = self.longestConsecutiveHelper(root.right)
        
        down, up = 0, 0
        node = root
        
        if node.left and node.left.val + 1 == root.val:
            down = max(down, left_down + 1)
            
        if node.left and node.left.val - 1 == root.val:
            up = max(up, left_up + 1)
            
        if node.right and node.right.val + 1 == root.val:
            down = max(down, right_down + 1)
            
        if node.right and node.right.val - 1 == root.val:
            up = max(up, right_up + 1)
            
            
        cur_len = down + 1 + up 
        
        max_len = max(cur_len, left_max_len, right_max_len)
        
        return max_len, down, up 
