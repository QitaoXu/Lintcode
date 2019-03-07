"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node 
"""


class BSTIterator:
    """
    @param: root: The root of binary tree.
    """

    """
    @return: True if there has next node, or false
    """
    def __init__(self, root):
        # do intialization if necessary
        self.stack = []
        
        while root:
            self.stack.append(root)
            root = root.left
        
    
    def hasNext(self, ):
        # write your code here
        return not len(self.stack) == 0

    """
    @return: return next node
    """
    def next(self, ):
        # write your code here
        
        if not self.hasNext():
            return None 
            
        node, result = self.stack[-1], self.stack[-1]
        
        if not node.right:
            
            node = self.stack.pop() 
            
            while len(self.stack) > 0 and self.stack[-1].right == node:
                node = self.stack.pop()
                
        else:
            
            node = node.right
            
            while node:
                self.stack.append(node)
                node = node.left
                
        return result   