public class VerticalOrder {
    
    public List<List<Integer>> verticalTraversal(TreeNode root) {
        
        List<Location> locations = new ArrayList<Location>();
        dfs(root, 0, 0, locations);
        Collections.sort(locations);
        
        List<List<Integer>> results = new ArrayList<List<Integer>>();
        results.add(new ArrayList<Integer>());
        
        int prev = locations.get(0).x; 
        
        for (Location loc : locations) {
            
            if (prev != loc.x) {
                
                results.add(new ArrayList<Integer>());
            }
            
            results.get(results.size() - 1).add(loc.val);
            prev = loc.x;
        }
        
        return results;
        
    }
    
    public void dfs(TreeNode root, int x, int y, List<Location> locations) {
        
        if (root == null) return; 
        
        locations.add(new Location(x, y, root.val));
        dfs(root.left, x - 1, y + 1, locations);
        dfs(root.right, x + 1, y + 1, locations);
    }
}

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

class Location implements Comparable<Location> {
    
    int x, y, val; 
    
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