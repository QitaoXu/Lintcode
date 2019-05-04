import sys 
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
    @return: the root of the maximum average of subtree
    """
    def __init__(self):
        self.maxAverage = - sys.maxsize
        self.maxRoot = None 
        
    def findSubtree2(self, root):
        # write your code here
        tree_size, tree_average = self.divideConquer(root)
        
        return tree_size, tree_average, self.maxRoot
    
    
    def divideConquer(self, root):
        
        if root == None:
            return 0, 0
            
        leftSize, leftAverage = self.divideConquer(root.left)
        rightSize, rightAverage = self.divideConquer(root.right)
        
        curSize = leftSize + rightSize + 1 
        curAverage = (leftSize * leftAverage + rightSize * rightAverage + root.val) / curSize
        
        if curAverage > self.maxAverage:
            self.maxAverage = curAverage
            self.maxRoot = root 
            
        return leftSize + rightSize + 1, curAverage
        
        