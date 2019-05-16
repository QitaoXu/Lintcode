"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    
    def __init__(self):
        
        self.tree_sum_to_count = {}
        self.max_count = -1 
        self.max_tree_sum = []
    """
    @param root: the root
    @return: all the values with the highest frequency in any order
    """
    def findFrequentTreeSum(self, root):
        # Write your code here
        
        self.findFrequentTreeSumHelper(root)
        
        return self.max_tree_sum
        
    def findFrequentTreeSumHelper(self, root):
        
        if root is None:
            
            return 0 
            
        left_sum = self.findFrequentTreeSumHelper(root.left)
        right_sum = self.findFrequentTreeSumHelper(root.right)
        
        cur_sum = left_sum + right_sum + root.val 
        
        self.tree_sum_to_count[cur_sum] = self.tree_sum_to_count.get(cur_sum, 0) + 1 
        
        if self.tree_sum_to_count[cur_sum] == self.max_count:
            self.max_tree_sum.append(cur_sum)
            
        elif self.tree_sum_to_count[cur_sum] > self.max_count:
            self.max_count = self.tree_sum_to_count[cur_sum]
            self.max_tree_sum.clear()
            self.max_tree_sum.append(cur_sum)
            
        return cur_sum
            