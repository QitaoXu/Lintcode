"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root):
        
        if root is None:
            return root 
        
        results = [] 
        
        self.helper(root, results)
        
        head = results[0]
        tail = results[-1]
        
        head.left = tail 
        tail.right = head 
        
        return head 
    
    def helper(self, root, results):
        
        if root is None:
            return 
        
        self.helper(root.left, results)
        
        results.append(root)
        
        if len(results) >= 2:
            
            prev = results[-2]
            curt = results[-1]
            
            prev.right = curt 
            curt.left = prev 
            
        self.helper(root.right, results)
        