import java.util.*; 

/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;

    public Node() {}

    public Node(int _val,List<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/
class Node {
    public int val;
    public List<Node> neighbors;

    public Node() {}

    public Node(int _val,List<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};

public class CloneGraph {
    public Node cloneGraph(Node node) {
        
        List<Node> nodes = this.getNodes(node);
        
        Map<Node, Node> map = new HashMap<Node, Node>(); 
        
        for (Node curt : nodes) {
            
            map.put(curt, new Node(curt.val, new ArrayList<Node>()));
        }
        
        for (Node curt : nodes) {
            
            Node newNode = map.get(curt); 
            
            for (Node neighbor : curt.neighbors) {
                
                Node newNeighbor = map.get(neighbor);
                newNode.neighbors.add(newNeighbor);
                
            }
        }
        
        return map.get(node);
    }
    
    private List<Node> getNodes(Node node) {
        
        Queue<Node> queue = new LinkedList<Node>(); 
        Set<Node> seen = new HashSet<Node>(); 
        List<Node> nodes = new ArrayList<Node>();
        
        queue.offer(node);
        seen.add(node);
        
        while (!queue.isEmpty()) {
            
            int size = queue.size(); 
            
            for (int i = 0; i < size; i++) {
                
                Node curt = queue.poll();
                nodes.add(curt);
                
                for (Node neighbor : curt.neighbors) {
                    
                    if (seen.contains(neighbor)) {
                        continue;
                    }
                    
                    queue.offer(neighbor);
                    seen.add(neighbor);
                    
                }
            }
        }
        
        return nodes;
        
    }
}