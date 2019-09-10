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

public class TreeInorderTraversal {


    public List<Integer> inorder(TreeNode root) {

        List<Integer> result = new ArrayList<Integer>(); 

        if (root == null) {
            return result;
        }

        Stack<TreeNode> stack = this.buildStack(root);

        while (!stack.isEmpty()) {

            result.add(stack.peek().val);
            this.moveUpper(stack);
        }

        return result;
    }

    private Stack<TreeNode> buildStack(TreeNode root) {

        Stack<TreeNode> stack = new Stack<TreeNode>();

        while (root != null) {

            stack.push(root); 

            root = root.left;
        }

        return stack;
    }

    private void moveUpper(Stack<TreeNode> stack) {

        TreeNode node = stack.peek(); 

        if (node.right == null) {

            node = stack.pop(); 

            while (!stack.isEmpty() && stack.peek().right == node) {
                node = stack.pop();
            }
        }

        else {

            node = node.right; 

            while (node != null) {
                stack.push(node);
                node = node.left;
            }
        }

    }
}