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
    @return: Inorder in ArrayList which contains node values.
    """

    def inorderTraversal(self, root):
        # write your code here

        stack = [] 
        result = [] 

        while root:
            stack.append(root)
            root = root.left


        while len(stack) > 0:

            node = stack[-1]
            result.append(node.val)

            if not node.right:

                node = stack.pop() 

                while len(stack) > 0 and stack[-1].right == node:
                    node = stack.pop() 

            else:

                node = node.right 

                while node:
                    stack.append(node)
                    node = node.left
        return result 



