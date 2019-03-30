"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum2(self, root, target):
        # write your code here
        result = []
        
        
        if root is None:
            return result
            
        path = [] 
        
        self.dfs(root, path, result, 0, target)
        return result
            
        
        
    def dfs(self, root, path, result, l, target):
        
        if root is None:
            return 
        
        path.append(root.val)
        
        tmp = target
        
        for i in range(l, -1, -1):
            
            tmp -= path[i]
            
            if tmp == 0:
                result.append(path[i:])
                
        self.dfs(root.left, path, result, l + 1, target)
        self.dfs(root.right, path, result, l + 1, target)
        
        path.pop()