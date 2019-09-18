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


public class BST {

    TreeNode root; 

    public BST() {
        this.root = null; 
    }

    public boolean search(int target) {

        return searchHelper(root, target);
    }

    private boolean searchHelper(TreeNode node, int target) {

        if (node == null) {
            return false;
        }

        if (node.val == target) {
            return true;
        }

        else if (node.val < target) {
            return this.searchHelper(node.right, target);
        }

        else {
            return this.searchHelper(node.right, target);
        }

    }

    public boolean insert(int target) {

        if (this.root == null) {

            this.root = new TreeNode(target);
            return true;
        }

        return this.insertHelper(root, target);
    }

    private boolean insertHelper(TreeNode node, int target) {

        if (target == node.val) {
            return false;
        }

        else if (target < node.val) {

            if (node.left == null) {
                node.left = new TreeNode(target);
                return true;
            }

            else {
                return this.insertHelper(node.left, target);
            }
        }

        else {

            if (node.right == null) {
                node.right = new TreeNode(target);
                return true;
            }

            else {
                return this.insertHelper(node.right, target);
            }
        }
    }
}