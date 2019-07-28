import java.util.*;

public class CourseScheduleII {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        
        HashMap<Integer, HashSet<Integer>> graph = this.buildGraph(prerequisites, numCourses); 
        
        return this.topoSorting(graph);
        
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
    
    private int[] topoSorting(HashMap<Integer, HashSet<Integer>> graph) {
        
        HashMap<Integer, Integer> indegrees = this.getIndegrees(graph);
        
        Queue<Integer> queue = new LinkedList<Integer>(); 
        
        for (Integer node : graph.keySet()) {
            
            if (indegrees.get(node) == 0) {
                queue.offer(node);
            }
        }
        
        ArrayList<Integer> order = new ArrayList<Integer>(); 
        
        while (!queue.isEmpty()) {
            
            int node = queue.poll();
            
            order.add(node);
            
            for (Integer neighbor : graph.get(node)) {
                
                indegrees.put(neighbor, indegrees.get(neighbor) - 1); 
                
                if (indegrees.get(neighbor) == 0) {
                    queue.offer(neighbor);
                }
            }
        }
        
        if (order.size() == graph.size()) {
            int[] result = new int[order.size()]; 
            
            for (int i = 0; i < order.size(); i++) {
                
                result[i] = order.get(i);
            }
            
            return result;
        }
        
        else {
            
            return new int[0];
        }
    }
}