import java.util.ArrayList;

public class setBitsPermutation{

    public static void main(String[] args) {

        Solution solution = new Solution(); 

        System.out.println(solution.findSetBitPermutationNumbers(1));
        
    }
}

class SetBitTable {

    private int[] table = new int[256]; 

    public SetBitTable() {

        for (int index = 0; index < 256; index++) {

            this.table[index] = index & 1 + table[index / 2]; 
        }
    
    }
    
    
    public int lookup(int num) {

        return this.table[num & 0xFF] + this.table[(num >> 8) & 0xFF] + this.table[(num >> 16) & 0xFF] + this.table[(num >> 24) & 0xFF]; 
    }
}

class Solution {

    public ArrayList<Integer> findSetBitPermutationNumbers(int num) {
        SetBitTable table = new SetBitTable();
        int setBitsNum =  table.lookup(num); 
        return this.setBitsPermutation(setBitsNum); 

    }

    private ArrayList<Integer> setBitsPermutation(int setBitsNum) {

        ArrayList<Integer> results = new ArrayList<>(); 
        ArrayList<Integer> permutation = new ArrayList<>(); 

        this.dfs(setBitsNum, 0, permutation, results); 
        
        return results; 
    }

    private void dfs(int setBitsNum, 
                     int index, 
                     ArrayList<Integer> permutation, 
                     ArrayList<Integer> results) {

            if (setBitsNum == 0) {

                results.add(this.bitsToNum(permutation)); 
                return; 
            }

            if (index == 31 || 31 - index < setBitsNum) {
                return; 
            }

            permutation.add(1); 
            this.dfs(setBitsNum - 1, index + 1, permutation, results); 
            permutation.remove(permutation.size() - 1); 

            permutation.add(0); 
            this.dfs(setBitsNum, index + 1, permutation, results); 
            permutation.remove(permutation.size() - 1); 

    }

    private int bitsToNum(ArrayList<Integer> bits) {

        int num = 0; 

        for (int index = bits.size() - 1; index >= 0; index--){

            num = num * 2 + bits.get(index);  
        }

        return num; 

    }

}

