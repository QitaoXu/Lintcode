public class PathSumII {
    public List<List<Integer>> pathSum(TreeNode root, int sum) {
        
        List<List<Integer>> results = new ArrayList<List<Integer>>(); 
        
        List<Integer> path = new ArrayList<Integer>();
        
        pathSumHelper(root, sum, path, results);
        
        return results;
        
    }
    
    private void pathSumHelper(TreeNode root, int sum, List<Integer> path, List<List<Integer>> results) {
        
        if (root == null) return; 
        
        if (root.left == null && root.right == null) {
            
            if (sum - root.val == 0) {
                path.add(root.val);
                results.add(new ArrayList<Integer>(path));
                path.remove(path.size() - 1);
            }
            
            return;
        }
        
        path.add(root.val);
        
        pathSumHelper(root.left, sum - root.val, path, results);
        pathSumHelper(root.right, sum - root.val, path, results);
        
        path.remove(path.size() - 1);
        
    }
}