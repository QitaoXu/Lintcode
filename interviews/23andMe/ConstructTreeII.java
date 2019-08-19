/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class ConstructTreeII {
    
    int postIndex; 
    int[] postorder;
    int[] inorder; 
    Map<Integer, Integer> indexMap = new HashMap<Integer, Integer>();
    
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        
        int index = 0; 
        this.inorder = inorder;
        this.postorder = postorder;
        this.postIndex = postorder.length - 1;
        
        for (Integer val : inorder) {
            
            indexMap.put(val, index++);
        }
        
        return helper(0, inorder.length - 1);
    } 
    
    private TreeNode helper(int inLeft, int inRight) {
        
        if (inLeft > inRight) {
            return null;
        }
        
        int rootVal = postorder[postIndex];
        TreeNode root = new TreeNode(rootVal); 
        
        int index = indexMap.get(rootVal);
        
        postIndex -= 1; 
        
        root.right = helper(index + 1, inRight);
        root.left = helper(inLeft, index - 1);
        
        return root;
    }
}

class TreeNode {

    int val; 
    TreeNode left; 
    TreeNode right; 

    public TreeNode(int val) {

        this.val = val; 
    }
}