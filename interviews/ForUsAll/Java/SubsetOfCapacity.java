import java.util.*;
public class SubsetOfCapacity{

    public boolean getSubsetOfCapacity(int capacity, int[] weights) {

        ArrayList<ArrayList<Integer>> results = new ArrayList<ArrayList<Integer>>(); 
        ArrayList<Integer> combination = new ArrayList<>();

        boolean res = this.dfs(capacity, weights, 0, 0, combination, results);

        System.out.println(combination);

        return res;
    }

    private boolean dfs(int capacity, 
                    int[]weights, 
                    int index, 
                    int sum,
                    ArrayList<Integer> combination,
                    ArrayList<ArrayList<Integer>> results) {

        
        if (sum % capacity == 0 && sum != 0) {

            results.add(new ArrayList<Integer>(combination));
            return true;

        }

        if (index == weights.length) {
            return false;
        }

        combination.add(weights[index]);
        if (this.dfs(capacity, weights, index + 1, sum + weights[index], combination, results)) 
            return true;
        combination.remove(combination.size() - 1);

        if (this.dfs(capacity, weights, index + 1, sum, combination, results)) 
            return true;

        return false;
    }

    public static void main(String[] args) {

        SubsetOfCapacity soc = new SubsetOfCapacity(); 

        int capacity = 3;
        int[] weights = {1, 3, 5, 21};

        System.out.println(soc.getSubsetOfCapacity(capacity, weights));
    }

}