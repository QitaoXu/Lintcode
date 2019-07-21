import java.util.*;

public class CourseSchedule {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        
        HashMap<Integer, HashSet<Integer>> graph = this.buildGraph(prerequisites, numCourses); 
        
        return this.topoSorting(graph);
        
    }
    
    private HashMap<Integer, HashSet<Integer>> buildGraph(int[][] prerequisties, int num) {
        
        HashMap<Integer, HashSet<Integer>> graph = new HashMap<>(); 
        
        for (int i = 0; i < num; i++) {
            graph.put(i, new HashSet<Integer>());
        }
        
        for (int[] pre : prerequisties) {
            
            graph.get(pre[1]).add(pre[0]);
        }
        
        return graph;
    }
    
    private HashMap<Integer, Integer> getIndegrees(HashMap<Integer, HashSet<Integer>> graph) {
        
        HashMap<Integer, Integer> indegrees = new HashMap<>(); 
        
        for (Integer i : graph.keySet()) {
            indegrees.put(i, 0);
        }
        
        for (Integer node : graph.keySet()) {
            
            for (Integer neighbor : graph.get(node)) {
                
                indegrees.put(neighbor, indegrees.get(neighbor) + 1);
            }
        }
        
        return indegrees;
    }
    
    private boolean topoSorting(HashMap<Integer, HashSet<Integer>> graph) {
        
        
        HashMap<Integer, Integer> indegrees = this.getIndegrees(graph); 
        
        Queue<Integer> queue = new LinkedList<Integer>();
        
        for (Integer node : graph.keySet()) {
            
            if (indegrees.get(node) == 0) {
                queue.offer(node);
            }
        }
        
        ArrayList<Integer> order = new ArrayList<>(); 
        
        while (!queue.isEmpty()) {
            
            int node = queue.poll(); 
            
            order.add(node);
            
            for (Integer neighbor : graph.get(node)) {
                
                indegrees.put(neighbor, indegrees.get(neighbor) - 1);
                
                if (indegrees.get(neighbor) == 0) queue.offer(neighbor);
            }
        }
        
        return order.size() == graph.size();
    }
}