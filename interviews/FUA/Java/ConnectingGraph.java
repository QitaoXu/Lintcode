import java.util.ArrayList;
import java.util.HashMap;

public class ConnectingGraph {
    
    HashMap<Integer, Integer> father;
    int count;
    /*
    * @param n: An integer
    */public ConnectingGraph(int n) {
        // do intialization if necessary
        this.father = new HashMap<Integer, Integer>();
        this.count = n; 
        
        for (int i = 1; i < n + 1; i++) {
            this.father.put(i, i);
        }
    }

    /*
     * @param a: An integer
     * @param b: An integer
     * @return: nothing
     */
    public void connect(int a, int b) {
        // write your code here
        
        int root_a = this.find(a);
        int root_b = this.find(b); 
        
        if (root_a == root_b) return;
        
        this.father.put(root_b, root_a); 
        this.count -= 1;
    }
    
    public int find(int point) {
        
        ArrayList<Integer> path = new ArrayList<>();
        
        while (point != this.father.get(point)) {
            
            path.add(point);
            point = this.father.get(point);
        }
        
        for (Integer p : path) {
            this.father.put(p, point);
        }
        return point;
    }

    /*
     * @param a: An integer
     * @param b: An integer
     * @return: A boolean
     */
    public boolean query(int a, int b) {
        // write your code here
        
        int root_a = this.find(a);
        int root_b = this.find(b);
        
        return root_a == root_b;
        
        
    }

    public static void main(String[] args) {

        ConnectingGraph cg = new ConnectingGraph(8);
        ArrayList<Boolean> results = new ArrayList<>();

        results.add(cg.query(1, 2));

        cg.connect(1, 2);

        results.add(cg.query(1, 3)); 

        cg.connect(2, 4);

        results.add(cg.query(1, 4));

        System.out.println(results);
    }
}