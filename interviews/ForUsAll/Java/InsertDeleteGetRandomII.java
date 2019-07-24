import java.util.*;
import java.util.Random;

class InsertDeleteGetRandomII {
    
    private ArrayList<Integer> nums;
    private HashMap<Integer, Set<Integer>> numToIdx;
    private Random rand;

    /** Initialize your data structure here. */
    public InsertDeleteGetRandomII() {
        
        this.nums = new ArrayList<Integer>();
        this.numToIdx = new HashMap<Integer, Set<Integer>>();
        this.rand = new Random();
        
    }
    
    /** Inserts a value to the collection. Returns true if the collection did not already contain the specified element. */
    public boolean insert(int val) {
        
        if (!this.numToIdx.containsKey(val)) {
            
            this.numToIdx.put(val, new LinkedHashSet<Integer>());
        }
        
        this.nums.add(val);
        this.numToIdx.get(val).add(this.nums.size() - 1);
        
        return this.numToIdx.get(val).size() == 1;
        
    }
    
    /** Removes a value from the collection. Returns true if the collection contained the specified element. */
    public boolean remove(int val) {
        
        if (!numToIdx.containsKey(val) || numToIdx.get(val).size() == 0) return false;
        
        int removeIdx = this.numToIdx.get(val).iterator().next();
        
        this.numToIdx.get(val).remove(removeIdx);
        
        int last = this.nums.get(this.nums.size() - 1);
        this.nums.set(removeIdx, last);
        this.numToIdx.get(last).add(removeIdx);
        this.numToIdx.get(last).remove(this.nums.size() - 1);
        
        this.nums.remove(this.nums.size() - 1);
        
        return true;
        
    }
    
    /** Get a random element from the collection. */
    public int getRandom() {
        
        return this.nums.get(this.rand.nextInt(this.nums.size()));
        
    }
}

/**
 * Your RandomizedCollection object will be instantiated and called as such:
 * RandomizedCollection obj = new RandomizedCollection();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */