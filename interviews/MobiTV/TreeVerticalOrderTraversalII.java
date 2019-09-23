/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

import java.util.*; 

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}

public class TreeVerticalOrderTraversalII {
    public List<List<Integer>> verticalTraversal(TreeNode root) {
        
        List<Location> locations = new ArrayList<Location>(); 
        
        dfs(root, 0, 0, locations);
        
        Collections.sort(locations);
        
        List<List<Integer>> results = new ArrayList<List<Integer>>();
        
        results.add(new ArrayList<Integer>());
        
        Integer prev = null; 
        
        for (Location location : locations) {
            
            if (prev != null && prev != location.x) {
                results.add(new ArrayList<Integer>());
            }
            
            results.get(results.size() - 1).add(location.val);
            prev = location.x;
        }
        
        return results;
        
    }
    
    private void dfs(TreeNode root, int x, int y, List<Location> locations) {
        
        if (root == null) {
            return; 
        }
        
        locations.add(new Location(x, y, root.val));
        dfs(root.left, x - 1, y + 1, locations);
        dfs(root.right, x + 1, y + 1, locations);
    }
    
    
}

class Location implements Comparable<Location> {
    
    int x; 
    int y; 
    int val; 
    
    public Location(int x, int y, int val) {
        
        this.x = x; 
        this.y = y; 
        this.val = val;
    }
    
    @Override 
    public int compareTo(Location that) {
        
        if (this.x != that.x) {
            return this.x - that.x; 
        }
        
        else if (this.y != that.y) {
            return this.y - that.y;
        }
        else {
            return this.val - that.val;
        }
    }
}