import java.util.*;
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

public class ClosestBST {
    public int closestValue(TreeNode root, double target) {
        
        Stack<TreeNode> lowerStack = this.getStack(root, target);
        Stack<TreeNode> upperStack = this.getStack(root, target);
        
        if (lowerStack.peek().val < target) {
            
            this.moveUpper(upperStack);
        }
        
        else {
            
            this.moveLower(lowerStack);
        }
        
        if (this.isLowerClose(lowerStack, upperStack, target)) {
            
            return lowerStack.peek().val;
        }
        else {
            return upperStack.peek().val;
        }
        
    }
            
    private Stack<TreeNode> getStack(TreeNode root, double target) {
        
        Stack<TreeNode> stack = new Stack<>(); 
        
        while (root != null) {
            
            stack.push(root); 
            
            if (target > root.val) {
                
                root = root.right;
            }
            
            else if (target < root.val) {
                root = root.left;
            }
            else {
                
                break;
            }
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
            
    private void moveLower(Stack<TreeNode> stack) {
        
        TreeNode node = stack.peek(); 
        
        if (node.left == null) {
            
            node = stack.pop(); 
            
            while (!stack.isEmpty() && stack.peek().left == node) {
                node = stack.pop();
            }
        }
        else {
            
            node = node.left; 
            
            while (node != null) {
                stack.push(node);
                node = node.right;
            }
        }
    }
            
    private boolean isLowerClose(Stack<TreeNode> lowerStack, Stack<TreeNode> upperStack, double target) {
        
        if (upperStack.isEmpty()) {
            return true;
        }
        
        if (lowerStack.isEmpty()) {
            return false;
        }
        
        return target - lowerStack.peek().val <= upperStack.peek().val - target;
    }
            
            
}