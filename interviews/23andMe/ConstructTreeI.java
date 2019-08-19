public class ConstructTreeI {
    
    int preIndex = 0;
    int[] preorder;
    int[] inorder;
    Map<Integer, Integer> indexMap = new HashMap<Integer, Integer>();
    
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        
        this.preorder = preorder;
        this.inorder = inorder; 
        
        int index = 0;
        for (Integer val : inorder) {
            indexMap.put(val, index++);
        }
        
        return this.helper(0, inorder.length - 1);
    }
    
    private TreeNode helper(int inLeft, int inRight) {
        
        if (inLeft > inRight) {
            return null;
        }
        
        int rootVal = preorder[preIndex];
        TreeNode root = new TreeNode(rootVal);
        
        int index = indexMap.get(rootVal); 
        
        preIndex += 1; 
        
        root.left = helper(inLeft, index - 1);
        root.right = helper(index + 1, inRight);
        
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