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
    @return: the value in the BST that is closest to the target
    """
    def __init__(self):
        self.closestDiff = sys.maxsize
        self.closestNode = None
        
    def closestValue(self, root, target):
        # write your code here
        if not root:
            return None 
        
        # self.traverse(root, target)
        
        # return self.closestNode.val
        
        lower_stack = self.get_stack(root, target)
        
        upper_stack = list(lower_stack)
        
        if lower_stack[-1].val < target:
            self.move_uppper(upper_stack)
            
        else:
            self.move_lower(lower_stack)
            
        
        if self.is_left_close(lower_stack, upper_stack, target):
            return lower_stack[-1].val 
            
        else:
            return upper_stack[-1].val
        
        
    def traverse(self, root, target):
        
        if root == None:
            return 
        
        self.traverse(root.left, target)
        
        diff = abs(root.val - target)
        
        if diff < self.closestDiff:
            self.closestDiff = diff 
            self.closestNode = root 
            
        self.traverse(root.right, target)
        
    def get_stack(self, root, target):
        
        stack = [] 
        
        while root:
            
            stack.append(root)
            
            if target < root.val:
                root = root.left
                
            elif target == root.val:
                break
                
            else:
                root = root.right
                
        return stack
        
    def move_uppper(self, stack):
        
        node = stack[-1]
        
        if node.right == None:
            
            node = stack.pop() 
            
            while stack and stack[-1].right == node:
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
            
            while stack and stack[-1].left == node:
                node = stack.pop() 
                
                
        else:
            node = node.left 
            
            while node:
                stack.append(node) 
                node = node.right 
                
    def is_left_close(self, lower_stack, upper_satck, target):
        
        if len(lower_stack) == 0:
            return False 
            
        elif len(upper_satck) == 0:
            return True 
            
        else:
            return target - lower_stack[-1].val <= upper_satck[-1].val - target
        
        
    
