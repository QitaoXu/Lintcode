import java.util.*;
import java.util.Random;

class InsertDeleteGetRandom {
    
    private ArrayList<Integer> nums;
    private HashMap<Integer, Integer> numToIndex;
    private Random rand;

    /** Initialize your data structure here. */
    public InsertDeleteGetRandom() {
        
        this.nums = new ArrayList<Integer>();
        this.numToIndex = new HashMap<Integer, Integer>();
        this.rand = new Random();
        
    }
    
    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    public boolean insert(int val) {
        
        if (this.numToIndex.containsKey(val)) return false; 
        
        this.nums.add(val);
        this.numToIndex.put(val, this.nums.size() - 1);
        return true;
        
    }
    
    /** Removes a value from the set. Returns true if the set contained the specified element. */
    public boolean remove(int val) {
        
        if (!this.numToIndex.containsKey(val)) return false; 
        
        int idx = this.numToIndex.get(val); 
        
        if (idx < this.nums.size() - 1) {
            
            int last = this.nums.get(this.nums.size() - 1);
            this.nums.set(idx, last);
            this.numToIndex.put(last, idx);
        }
        
        this.nums.remove(this.nums.size() - 1);
        this.numToIndex.remove(val);
        
        return true;
        
    }
    
    /** Get a random element from the set. */
    public int getRandom() {
        
        return this.nums.get(this.rand.nextInt(this.nums.size()));
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */