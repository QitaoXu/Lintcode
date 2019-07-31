import java.util.*;

public class GraphHasCycle {

    public boolean detectCycles(HashMap<Integer, HashSet<Integer>> graph) {

        HashMap<Integer, Integer> indegrees = this.getIndegrees(graoh);

        Queue<Integer> queue = new LinkedList<Integer>(); 

        for (Integer node : graph.keySet()) {

            if (indegrees.get(node) == 0) {
                queue.offer(node);
            }
        }

        int count = 0; 

        while(!queue.isEmpty()) {
            
            int node = queue.poll(); 

            for (Integer neighbor : graph.get(node)) {

                indegrees.put(neighbor, indegrees.get(neighbor) - 1); 

                if (indegrees.get(neighbor) == 0) {

                    queue.offer(neighbor);
                }
            }
            
            count += 1;
        }

        if (count != graph.size()) return true;
        else return false;
        
    }

    private HashMap<Integer, Integer> getIndegrees(HashMap<Integer, HashSet<Integer>> graph) {

        HashMap<Integer, Integer> indegrees = new HashMap<>();

        for (Integer node : graph.keySet()) {

            indegrees.put(node, 0);
        }

        for (Integer node : graph.keySet()) {

            for (Integer neighbor : graph.gey(node)) {

                indegrees.put(neighbor, indegrees.get(neighbor) + 1);
            }
        }

        return indegrees;
    }


}