import java.util.*; 

class TreeNode {

    int val; 
    TreeNode left; 
    TreeNode right; 

    public TreeNode(int val) {
        this.val = val; 
        this.left = null; 
        this.right = null;
    }
}

public class VerticalOrder {
    public List<List<Integer>> verticalOrder(TreeNode root) {
        
        List<List<Integer>> res = new ArrayList<List<Integer>>(); 
        
        if (root == null) 
            return res; 
        
        Map<Integer, List<Integer>> map = new TreeMap<Integer, List<Integer>>();
        Queue<TreeNode> queue = new LinkedList<TreeNode>(); 
        Queue<Integer> colQueue = new LinkedList<Integer>(); 
        
        queue.offer(root);
        colQueue.offer(0); 
        
        while (!queue.isEmpty()) {
            
            int size = queue.size(); 
            
            for (int i = 0; i < size; i++) {
                
                TreeNode node = queue.poll();
                int col = colQueue.poll();
                
                if (!map.containsKey(col)) {
                    map.put(col, new ArrayList<Integer>());
                }
                
                map.get(col).add(node.val);
                
                if (node.left != null) {
                    queue.offer(node.left);
                    colQueue.offer(col - 1);
                }
                
                if (node.right != null) {
                    queue.offer(node.right);
                    colQueue.offer(col + 1);
                }
            }
        }
        
        for (Integer col : map.keySet()) {
            
            res.add(map.get(col));
        }
        
        return res;
    }
}