class Solution:

    def isCousin(self, root, node1, node2):

        grandParent1, parent1 = self.helper(root, node1, None, None)
        grandParent2, parent2 = self.helper(root, node2, None, None)

        if grandParent1 and grandParent2:

            if grandParent1 == grandParent2 and parent1 != parent2:

                return True 

        return False 

    def helper(self, root, target, parent, grandParent):

        if root is None:

            return None, None 

        if root == target:

            return grandParent, parent

        leftG, leftP = self.helper(root.left, target, root, parent)
        rightG, rightP = self.helper(root.right, target, root, parent)

        if leftG:

            return leftG, leftP

        else:

            return rightG, rightP

