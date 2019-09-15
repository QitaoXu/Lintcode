public class SplitArrayLargestSum {
    public int splitArray(int[] nums, int m) {
        
        int n = nums.length; 
        
        int[][] dp = new int[n + 1][m + 1]; 
        
        for (int i = 0; i < n + 1; i++) {
            for (int j = 0; j < m + 1; j++) {
                dp[i][j] = Integer.MAX_VALUE; 
            }
        }
        
        dp[0][0] = 0; 
        
        int[] prefixsum = new int[n + 1];
        
        for (int i = 0; i < n; i++) {
            prefixsum[i + 1] = nums[i] + prefixsum[i];
        }
        
        for (int i = 1; i < n + 1; i++) {
            for (int j = 1; j < m + 1; j++) {
                for (int k = 0; k < i; k++) {
                    
                    dp[i][j] = Math.min(dp[i][j], Math.max(prefixsum[i] - prefixsum[k], dp[k][j - 1]));
                }
            }
        }
        
        return dp[n][m];
        
    }
    
    
}