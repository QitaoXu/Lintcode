public class RemoveDuplicatesFromSortedArray {
    public int removeDuplicates(int[] nums) {
        
        int count = 0; 
        
        if (nums == null || nums.length == 0) return count; 
        
        for (int i = 0; i < nums.length; i++) {
            
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            
            nums[count++] = nums[i];
            
        }
        
        return count;
        
    }
}