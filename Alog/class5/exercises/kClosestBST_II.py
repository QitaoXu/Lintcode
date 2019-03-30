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
    @param target: the given target
    @param k: the given k
    @return: k values in the BST that are closest to the target
    """
    def closestKValues(self, root, target, k):
        # write your code here
        
        # _satck = [] 
        if root is None or k == 0:
            return []
            
        lower_stack = self.get_stack(root, target)
        upper_stack = list(lower_stack)
        
        if lower_stack[-1].val < target:
            self.move_upper(upper_stack)
        else:
            self.move_lower(lower_stack)
            
        result = []
        for _ in range(k):
            
            if self.is_lower_close(lower_stack, upper_stack, target):
                result.append(lower_stack[-1].val)
                self.move_lower(lower_stack)
                
            else:
                result.append(upper_stack[-1].val)
                self.move_upper(upper_stack)
                
        return result
                
            
        
        
    def get_stack(self, root, target):
        
        stack = []
        
        while root:
            
            stack.append(root)
            
            if target < root.val:
                root = root.left
                
            elif target == root.val:
                break
            
            elif target > root.val:
                root = root.right
                
        return stack
        
    def move_upper(self, stack):
        
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
        
    def move_lower(self, stack):
        node = stack[-1]
        
        if node.left == None:
            node = stack.pop() 
            
            while len(stack) > 0 and stack[-1].left == node:
                node = stack.pop()
                
        else:
            
            node = node.left 
            
            while node:
                stack.append(node)
                node = node.right
                
    def is_lower_close(self, lower_satck, upper_satck, target):
        
        if len(lower_satck) < 1:
            return False 
            
        if len(upper_satck) < 1:
            return True 
            
        return target - lower_satck[-1].val <= upper_satck[-1].val - target
