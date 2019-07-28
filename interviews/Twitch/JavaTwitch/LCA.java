import java.util.*; 

class TreeNode {

    int val; 
    TreeNode left;
    TreeNode right; 

    public TreeNode(int val) {

        this.val = val; 
        this.left = null; 
        this.right = null; 
    }
}

public class LCA {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        
        if (root == null) return null; 
        
        if (root == p || root == q) return root; 
        
        TreeNode leftLca = this.lowestCommonAncestor(root.left, p, q);
        TreeNode rightLca = this.lowestCommonAncestor(root.right, p, q);
        
        if (leftLca != null && rightLca != null) return root; 
        
        else if (leftLca != null) return leftLca; 
        
        else if (rightLca != null) return rightLca; 
        
        return null;
        
    }
}