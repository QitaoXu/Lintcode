import java.uti.*; 

public class ThreeSum {
    public List<List<Integer>> threeSum(int[] nums) {
        
        List<List<Integer>> results = new ArrayList<List<Integer>>(); 
        
        if (nums == null || nums.length < 3) return results; 
        
        Arrays.sort(nums); 
        
        for (int i = 0; i < nums.length - 2; i++) {
            
            if (i > 0 && nums[i] == nums[i - 1]) continue; 
            
            int target = -nums[i]; 
            int start = i + 1, end = nums.length - 1; 
            
            while (start < end) {
                
                if (nums[start] + nums[end] < target) {
                    start += 1;
                }
                else if (nums[start] + nums[end] > target) {
                    end -= 1;
                }
                
                else {
                    
                    List<Integer> result = new ArrayList<Integer>(); 
                    result.add(nums[i]);
                    result.add(nums[start]);
                    result.add(nums[end]);
                    
                    results.add(result); 
                    
                    start += 1; 
                    while (start < end && nums[start] == nums[start - 1]) {
                        start += 1;
                    }
                    
                    end -= 1; 
                    while (start < end && nums[end] == nums[end + 1]) {
                        end -= 1;
                    }
                }
            }
        }
        
        return results;
    }
}