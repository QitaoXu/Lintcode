public class SearchInRotatedSortedArrayII {
    public boolean search(int[] nums, int target) {
        
        if (nums == null || nums.length == 0) {
            return false;
        }
        
        int start = 0, end = nums.length - 1; 
        
        while (start + 1 < end) { 
            
            int mid = start + (end - start) / 2; 
            
            if (nums[mid] > nums[end]) {
                
                if (target >= nums[start] && target <= nums[mid]) {
                    
                    end = mid;
                }
                
                else {
                    start = mid;
                }
            }
            
            else {
                
                if (target >= nums[mid] && target <= nums[end]) {
                    
                    start = mid;
                }
                
                else {
                    end = mid;
                }
            }
        }
        
        if (nums[start] == target) {
            return true;
        }
        
        if (nums[end] == target) {
            return true;
        }
        
        for (int i = 0; i < nums.length; i++) {
            
            if (nums[i] == target) {
                return true;
            }
        }
        
        return false;
        
    }
}