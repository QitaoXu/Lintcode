import java.util.*;
// import java.util.HashSet;
// import java.util.List;
// import java.util.ArrayList;
// import java.util.LinkedList;
// import java.util.Stack;
// import java.util.Queue;


public class RemoveInvalidParentheses {
    public List<String> removeInvalidParentheses(String s) {
        
        List<String> results = new ArrayList<String>();
        
        if (this.isValid(s)) {
            results.add(s);
            return results;
        }
        
        Queue<String> queue = new LinkedList<String>();
        HashSet<String> visited = new HashSet<String>();
        
        queue.offer(s);
        visited.add(s); 
        
        while (!queue.isEmpty()) {
            
            int size = queue.size();
            
            if (results.size() > 0) return results;
            
            for (int i = 0; i < size; i++) {
                
                String node = queue.poll();
                
                for (String neighbor : this.getNeighbors(node)) {
                    
                    if (visited.contains(neighbor)) continue; 
                    
                    if (this.isValid(neighbor)) results.add(neighbor);
                    
                    queue.offer(neighbor);
                    visited.add(neighbor);
                }
            }
        }
        
        return results;
        
    }
    
    private List<String> getNeighbors(String node) {
        
        List<String> neighbors = new ArrayList<String>();
        
        for (int i = 0; i < node.length(); i++) {
            
            String neighbor = node.substring(0, i) + node.substring(i + 1);
            
            neighbors.add(neighbor);
            
        }
        
        return neighbors;
        
    }
    
    private boolean isValid(String node) {
        
        char[] node_arr = node.toCharArray();
        Stack<Character> stack = new Stack<>();
        
        for (Character c : node_arr) {
            
            if (c == '(') {
                stack.push(c);
            }
            
            else if (c == ')') {
                
                if (stack.size() == 0) return false;
                
                else stack.pop();
            }
            else continue;
            
        }
        
        return stack.size() == 0;
    }

    public static void main(String[] args) {

        RemoveInvalidParentheses rip = new RemoveInvalidParentheses(); 

        System.out.println(rip.removeInvalidParentheses("()())()"));

    }
}