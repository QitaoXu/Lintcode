import java.util.*;
public class FourSum {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        
        List<List<Integer>> results = new ArrayList<List<Integer>>();
        
        if (nums == null || nums.length < 4) return results;
        
        Arrays.sort(nums);
        
        for (int i = 0; i < nums.length - 3; i++) {
            
            if (i > 0 && nums[i] == nums[i - 1]) continue; 
            
            for (int j = i + 1; j < nums.length - 2; j++) {
                
                if (j > i + 1 && nums[j] == nums[j - 1]) continue; 
                
                int start = j + 1, end = nums.length - 1; 
                int targetSum = target - nums[i] - nums[j]; 
                
                while (start < end) {
                    
                    if (nums[start] + nums[end] < targetSum) {
                        start += 1;
                    }
                    
                    else if (nums[start] + nums[end] > targetSum) {
                        end -= 1;
                    }
                    
                    else {
                        
                        List<Integer> result = new ArrayList<Integer>(); 
                        result.add(nums[i]);
                        result.add(nums[j]);
                        result.add(nums[start]);
                        result.add(nums[end]);
                        
                        results.add(result);
                        
                        start += 1; 
                        while (start < end && nums[start] == nums[start - 1]) start += 1;
                        
                        end -= 1;
                        while (start < end && nums[end] == nums[end + 1]) end -= 1;
                    }
                }
            }
            
            
        }
        
        return results;
        
    }
}