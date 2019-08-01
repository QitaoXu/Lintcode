public class MoveZeroes {
    public void moveZeroes(int[] nums) {
        
        if (nums == null || nums.length == 0) return; 
        
        int left = 0, right = 0; 
        
        while (right < nums.length) {
            
            if (nums[right] != 0) {
                
                int temp = nums[right];
                nums[right] = nums[left];
                nums[left] = temp;
                left += 1;
            }
            
            right += 1;
        }
        
    }
}