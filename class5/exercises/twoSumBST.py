"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param: : the root of tree
    @param: : the target sum
    @return: two numbers from tree which sum is n
    """

    def twoSum(self, root, n):
        # write your code here
        if not root:
            return None
        target = n 
        lower_stack = self.get_lower_stack(root)
        upper_stack = self.get_upper_stack(root)
        
        while lower_stack[-1] != upper_stack[-1]:
            
            if lower_stack[-1].val + upper_stack[-1].val < target:
                self.move_upper(lower_stack)
                
            elif lower_stack[-1].val + upper_stack[-1].val == target:
                break
            
            else:
                self.move_lower(upper_stack)
                
        result = []
        if lower_stack[-1].val + upper_stack[-1].val == target:
            result.append(lower_stack[-1].val)
            result.append(upper_stack[-1].val)
            
            return result
        
        return None
        
    def get_lower_stack(self, root):
        
        stack = [] 
        
        while root:
            
            stack.append(root)
            
            root = root.left 
            
        return stack
        
    def get_upper_stack(self, root):
        stack = []
        
        while root:
            
            stack.append(root)
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