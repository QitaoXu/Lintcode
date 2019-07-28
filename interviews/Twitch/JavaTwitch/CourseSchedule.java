import java.util.*; 

public class CourseSchedule {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        
        HashMap<Integer, HashSet<Integer>> graph = this.buildGraph(prerequisites, numCourses); 
        
        return topo_sorting(graph);
        
    }
    
    private HashMap<Integer, HashSet<Integer>> buildGraph(int[][] pres, int num) {
        
        HashMap<Integer, HashSet<Integer>> graph = new HashMap<Integer, HashSet<Integer>>(); 
        
        for (int i = 0; i < num; i++) {
            
            graph.put(i, new HashSet<Integer>());
        }
        
        for (int[] pre : pres) {
            
            graph.get(pre[1]).add(pre[0]);
            
        }
        
        return graph;
    }
    
    private HashMap<Integer, Integer> getIndegrees(HashMap<Integer, HashSet<Integer>> graph) {
        
        HashMap<Integer, Integer> indegrees = new HashMap<>(); 
        
        for (Integer node : graph.keySet()) {
            
            indegrees.put(node, 0);
        }
        
        for (Integer node : graph.keySet()) {
            
            for (Integer neighbor : graph.get(node)) {
                
                indegrees.put(neighbor, indegrees.get(neighbor) + 1);
            }
        }
        
        return indegrees;
    }
    
    private boolean topo_sorting(HashMap<Integer, HashSet<Integer>> graph) {
        
        HashMap<Integer, Integer> indegrees = this.getIndegrees(graph);
        
        Queue<Integer> queue = new LinkedList<Integer>(); 
        
        for (Integer node : graph.keySet()) {
            
            if (indegrees.get(node) == 0) {
                
                queue.offer(node);
            }
        }
        
        List<Integer> order = new ArrayList<Integer>(); 
        
        while (!queue.isEmpty()) {
            
            int node = queue.poll(); 
            
            order.add(node); 
            
            for (int neighbor : graph.get(node)) {
                
                indegrees.put(neighbor, indegrees.get(neighbor) - 1);
                
                if (indegrees.get(neighbor) == 0) {
                    queue.offer(neighbor);
                }
            }
        }
        
        
        return order.size() == graph.size();
        
    }
}