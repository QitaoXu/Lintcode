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
    @param root: A Tree
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    """
    def zigzagLevelOrder(self, root):
        # write your code here
        if root is None:
            return [] 
            
        queue = deque() 
        
        result = [] 
        
        queue.append(root)
        
        level_count = 0
        
        while queue:
            
            size = len(queue)
            
            level = []
            
            level_count += 1 
            
            for _ in range(size):
                
                head = queue.popleft() 
                
                level.append(head.val) 
                    
                if head.left != None:
                    queue.append(head.left)
                    
                if head.right != None:
                    queue.append(head.right)
            
            if level_count % 2 == 1:     
                result.append(level)
                
            else:
                
                level = level[::-1]
                
                result.append(level)
            
        return result