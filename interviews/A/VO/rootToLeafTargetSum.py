class Solution:

    def findPathOfTarget(self, root, target):

        results = [] 
        
        if not root: 
            return results

        self.findPathOfTargetHelper(root, [root.val], target - root.val, results)

        return results

    
    def findPathOfTargetHelper(self, root, combination, target, results):

        if target == 0:
            results.append(combination.copy())
        
        if root is None: 
            return 

        for child in [root.left, root.right]: 

            combination.append(child.val) 

            self.findPathOfTargetHelper(child, combination, target - child.val, results)

            combination.pop()

        