import java.util.*; 

public class CombinationSumII {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        
        List<List<Integer>> results = new ArrayList<List<Integer>>();
        List<Integer> combination = new ArrayList<Integer>();
        
        Arrays.sort(candidates);
        
        dfs(candidates, 0, target, combination, results);
        
        return results;
        
    }
    
    private void dfs(int[] nums,
                     int startIndex, 
                     int target, 
                     List<Integer> combination,
                     List<List<Integer>> results) {
        
        if (target == 0) {
            
            results.add(new ArrayList<Integer>(combination)); 
            return; 
        }
        
        for (int i = startIndex; i < nums.length; i++) {
            
            if (i != startIndex && nums[i] == nums[i - 1]) continue;
            
            if (target - nums[i] < 0) break; 
            
            combination.add(nums[i]);
            dfs(nums, i + 1, target - nums[i], combination, results);
            combination.remove(combination.size() - 1);
        }
    }
}