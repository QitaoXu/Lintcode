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
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        # write your code here
        
        results = [] 
        
        if not root:
            return results 
        
        queue = deque()
        
        queue.append(root)
        
        while queue:
            
            size = len(queue)
            
            level = []
            
            for _ in range(size):
                
                node = queue.popleft()
                
                level.append(node.val)
                
                for neighbor in [node.left, node.right]:
                    
                    if neighbor:
                        queue.append(neighbor)
                       
            results.append(level)
            
        return results 