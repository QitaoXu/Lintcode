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

public class LCAOfBST {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        
        if (root == null) return null; 
        
        if (root.val < Math.min(p.val, q.val)) {
            
            return this.lowestCommonAncestor(root.right, p, q);
        }
        
        else if (root.val > Math.max(p.val, q.val)) {
            
            return this.lowestCommonAncestor(root.left, p, q);
        }
        
        else {
            
            return root;
        }
        
    }
}