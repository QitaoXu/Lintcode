class TreeNode:

    def __init__(self, val):

        self.val = val
        self.left = None 
        self.right = None 

class Solution:

    def findClosestBSTValue(self, root, target):

        lower_stack = self.get_stack(root, target)
        upper_stack = list(lower_stack) 

        if lower_stack[-1].val < target: 
            self.move_upper(upper_stack) 

        else:
            self.move_lower(lower_stack)

        if self.is_lower_lose(lower_stack, upper_stack, target):
            return lower_stack[-1].val 

        else:
            return upper_stack[-1].val 

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

    def move_upper(self, stack):

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

    def is_lower_lose(self, lower_stack, upper_stack, target):

        if len(upper_stack) == 0:
            return True 

        elif len(lower_stack) == 0:
            return False 

        else:

            return target - lower_stack[-1].val < upper_stack[-1].val - target 

