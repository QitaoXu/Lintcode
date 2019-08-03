public class FirstAndLastPosInSortedArray {
    public int[] searchRange(int[] nums, int target) {
        
        int[] res = {-1, -1};
        
        if (nums == null || nums.length == 0) {
            return res;
        }
        
        if (nums.length == 0 && nums[0] == target) {
            
            res[0] = 0;
            res[1] = 0;
            return res;
        }
        
        
        int left = getLastSmallerIndex(nums, target);
        int right = getFirstLargerIndex(nums, target);
        
        if ( left + 1 == right) {
            return res;
        }
        
        else{
        
            res[0] = left + 1;
            res[1] = right - 1;
        }
        
        return res;
        
    }
    
    private int getLastSmallerIndex(int[] nums, int target) {
        
        int start = 0, end = nums.length - 1; 
        
        while (start + 1 < end) {
            
            int mid = start + (end - start) / 2;
            
            if (nums[mid] < target) {
                
                start = mid;
            }
            
            else {
                
                end = mid;
            }
        }
        
        if (nums[end] < target) return end;
        
        if (nums[start] < target) return start;
        
        // All elements in nums are greater than or equal to target
        return -1;
    }
    
    private int getFirstLargerIndex(int[] nums, int target) {
        
        int start = 0, end = nums.length - 1; 
        
        while (start + 1 < end) {
            
            int mid = start + (end - start) / 2; 
            
            if (nums[mid] <= target) {
                
                start = mid;
            }
            
            else {
                end = mid;
            }
        
        }
        
        if (nums[start] > target) return start;
        
        if (nums[end] > target) return end;
        
        // All elements in nums are samller than or equal to target
        return nums.length;
    }
}