class PathSumIII {
    public int getPathSum(TreeNode root, int sum) {
        
        if (root == null) return 0;
        
        return getPathSum(root.left, sum) + getPathSum(root.right, sum) + pathSumHelper(root, sum);
        
    }
    
    private int pathSumHelper(TreeNode root, int sum) {
        
        int count = 0; 
        
        if (root == null) return 0; 
        
        if (sum == root.val) count += 1; 
        
        count += pathSumHelper(root.left, sum - root.val); 
        count += pathSumHelper(root.right, sum - root.val); 
        
        return count;
    }
}