public class JumpGame {
    public boolean canJump(int[] nums) {
        
        int n = nums.length; 
        
        if (n == 1) return true;
        
        boolean[] dp = new boolean[n];
        
        dp[n - 1] = true;
        
        for (int i = n - 2; i >= 0; i--) {
            
            for (int step = nums[i]; step >= 1; step--) {
                
                if (i + step > n - 1) continue; 
                
                if (dp[i + step]) {
                    
                    dp[i] = true;
                    break;
                }
            }
        }
        
        return dp[0];
    }
}