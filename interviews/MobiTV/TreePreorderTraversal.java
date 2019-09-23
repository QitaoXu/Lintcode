import java.util.*; 

class TreeNode {

    TreeNode left; 
    TreeNode right; 
    int val; 

    public TreeNode(int val) {
        this.left = null; 
        this.right = null; 
        this.val = val; 
    }
}
public class TreePreorderTraversal {
    public List<Integer> preorderTraversal(TreeNode root) {
        
        
        List<Integer> res = new ArrayList<Integer>(); 
        
        if (root == null) 
            return res; 
        
        Stack<TreeNode> stack = new Stack<TreeNode>(); 
        
        stack.push(root); 
        
        while (!stack.isEmpty()) {
            
            TreeNode node = stack.pop(); 
            
            res.add(node.val); 
            
            if (node.right != null) {
                stack.push(node.right);
            }
            
            if (node.left != null) {
                stack.push(node.left);
            }
        }
        
        return res;
        
    }
}