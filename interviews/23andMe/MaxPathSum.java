/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}

class MaxPathSum {
    int maxSum = Integer.MIN_VALUE; 
    
    public int maxPathSum(TreeNode root) {
        
        maxGain(root);
        return maxSum;
    }
    
    private int maxGain(TreeNode root) {
        
        if (root == null) {
            return 0;
        }
        
        int leftGain = Math.max(maxGain(root.left), 0);
        int rightGain = Math.max(maxGain(root.right), 0);
        
        int priceNewPath = root.val + leftGain + rightGain; 
        
        maxSum = Math.max(maxSum, priceNewPath);
        
        return root.val + Math.max(leftGain, rightGain);
    }
}