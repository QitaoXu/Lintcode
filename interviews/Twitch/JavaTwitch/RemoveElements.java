public class RemoveElements {
    public int removeElement(int[] nums, int val) {
        
        int i = 0;
        int n = nums.length - 1; 
        
        while (i <= n) {
            
            if (nums[i] == val) {
                
                nums[i] = nums[n];
                n--;
            }
            
            else {
                i++;
            }
        }
        
        return n + 1;
        
    }
}