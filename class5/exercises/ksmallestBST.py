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
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kthSmallest(self, root, k):
        # write your code here
        
        stack = [] 
        
        while root:
            stack.append(root)
            root = root.left 
            
        for _ in range(k - 1):
            
            if len(stack) == 0:
                break
            
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
        
        return stack[-1].val            