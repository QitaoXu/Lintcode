class Solution:

    def findGrandParents(self, root):

        results = [] 
        self.findGrandParentsHelper( root, None, None, results) 

        return results

    def findGrandParentsHelper(self, root, parent, grandParent, results):

        if root is None:
            return 

        if not root.left and not root.right: # this is a leaf node 

            if grandParent:
                results.append((root, grandParent)) # (leaf, grandParent)
            elif parent:
                results.append((root, parent))
            else:
                results.append((root, root))
            return 

        self.findGrandParentsHelper(root.left, root, parent, results) # find left subtree
        self.findGrandParentsHelper(root.right, root, parent, results) # find right subtree



