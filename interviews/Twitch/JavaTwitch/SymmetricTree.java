class TreeNode {
    
    int val; 
    TreeNode left;
    TreeNode right;

    public TreeNode (int val) {

        this.val = val;
        this.left = null;
        this.right = null;
    }
}
public class SymmetricTree {
    public boolean isSymmetric(TreeNode root) {
        
        return root == null || this.helper(root.left, root.right);
        
    }
    
    private boolean helper(TreeNode left, TreeNode right) {
        
        if (left == null || right == null) {
            
            return left == right;
        }
        
        if (left.val != right.val) {
            return false;
        }
        
        return this.helper(left.left, right.right) && this.helper(left.right, right.left);
    }
}