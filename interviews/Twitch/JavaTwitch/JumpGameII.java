import java.util.*; 
public class JumpGameII {
    public int jump(int[] nums) {
        
        int n = nums.length; 
        
        if (nums.length == 1) return 0;
        
        if (nums.length == 2) return 1;
        
        int[] dp = new int[n];
        
        Arrays.fill(dp, n);
        
        dp[n - 1] = 0; 
        
        for (int i = n - 2; i >= 0; i--) {
            
            for (int step = nums[i]; step >= 1; step--) {
                
                if (i + step > n - 1) continue;
                
                dp[i] = Math.min(dp[i], dp[i + step] + 1);
                
            }
        }
        
        return dp[0];
        
    }
}