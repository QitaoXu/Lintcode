class TreeNode:

    def __init__(self, val):
        self.val = val 
        self.left = None 
        self.right = None 

class Solution:

    def findNextGraterNode(self, root, val):

        stack = self.getStack(root, val) 

        node = stack[-1] 

        if node.right is None:

            node = stack.pop() 

            while stack and stack[-1].right == node:
                node = stack.pop()

        else:

            node = node.right 

            while node:

                stack.append(node) 

                node = node.left 

        return stack[-1].val 


    def getStack(self, root, val):

        stack = [] 

        while root:

            stack.append(root) 

            if val < root.val:

                root = root.left 

            elif val > root.val:

                root = root.right 

            else:

                break 

        return stack 

        