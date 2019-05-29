class TreeNode:

    def __init__(self, val):
        self.val = val 
        self.children = set() 

class Solution:

    def buildTree(self, nodesNums):

        return self.buildTreeHelper(0, nodesNums)

    
    def buildTreeHelper(self, start_index, nodesNums):

        if nodesNums[start_index] == 0:
            return TreeNode(0)

        root = TreeNode(nodesNums[start_index])

        for i in range(1, nodesNums[start_index] + 1):

            root.children.add(self.buildTreeHelper(start_index + i, nodesNums))

        return root 



