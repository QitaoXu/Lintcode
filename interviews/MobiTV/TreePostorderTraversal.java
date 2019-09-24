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

public class TreePostorderTraversal {
    public List<Integer> postorderTraversal(TreeNode root) {
        
        List<Integer> results = new ArrayList<Integer>(); 
        
        TreeNode prev = null; 
        TreeNode curt = root; 
        
        if (root == null) {
            return results;
        }
        
        Stack<TreeNode> stack = new Stack<TreeNode>();
        stack.push(root);
        
        while (!stack.isEmpty()) {
            
            curt = stack.peek();
            
            if (prev == null || prev.left == curt || prev.right == curt) {
                
                if (curt.left != null) {
                    stack.push(curt.left);
                } else if (curt.right != null) {
                    stack.push(curt.right);
                }
            }
            else if (curt.left == prev) {
                
                if (curt.right != null) {
                    stack.push(curt.right);
                }
            }
            else {
                
                results.add(curt.val);
                stack.pop();
            }
            
            prev = curt;
        }
        
        return results;
        
    }
}