class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root):
        # write your code here
        self.helper(root)
        
    # return the last node of the subtree root satanding for when traversed inorderly    
    def helper(self, root):
        
        
        if root == None:
            return None 
        
        left_last = self.helper(root.left)
        right_last = self.helper(root.right)
        
        if left_last is not None:
            
            left_last.right = root.right 
            root.right = root.left
            root.left = None 
            
        if right_last is not None:
            return right_last
            
        if left_last is not None:
            
            return left_last
            
        
        return root 