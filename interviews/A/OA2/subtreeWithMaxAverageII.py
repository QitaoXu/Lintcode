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
        
    def findSubtree2(self, root, k):
        # write your code here
        tree_size, tree_average = self.divideConquer(root, k)
        
        return tree_size, tree_average, self.maxRoot
    
    
    def divideConquer(self, root, k):
        
        if root == None:
            return 0, 0
            
        cur_size = 0
        cur_sum = 0 
        cur_average = 0 

        for child in root.children:

            k_size, k_average = self.divideConquer(child, k)

            cur_size += k_size 
            cur_sum += k_size * k_average

        cur_size += 1 
        cur_sum += root.val 
        cur_average = cur_sum / cur_average

        if cur_average > self.maxAverage:
            self.maxAverage = cur_average
            self.maxRoot = root 

        return cur_size, cur_average