public class LongestIncreasingSubsequence {
    public int lengthOfLIS(int[] nums) {
        
        if (nums == null || nums.length == 0) {
            return 0;
        }
        
        int n = nums.length;
        
        int[] dp = new int[n];
        
        int res = 0;
        
        Arrays.fill(dp, 1);
        
        for (int i = 0; i < n; i++) {
            
            for (int j = 0; j < i; j++) {
                
                if (nums[j] < nums[i]) {
                    
                    dp[i] = dp[i] > dp[j] ? dp[i] : dp[j] + 1;
                }
            }
            
            res = Math.max(dp[i], res);
        }
        
        return res;
    }
}