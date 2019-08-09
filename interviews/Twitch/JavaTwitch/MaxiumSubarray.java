public class MaxiumSubarray {
    public int maxSubArray(int[] nums) {
        
        if (nums == null || nums.length == 0) {
            return 0;
        }
        
        int n = nums.length; 
        
        int prefixSum = 0, minSum = 0, maxSum = Integer.MIN_VALUE;
        
        for (int i = 0; i < n; i++) {
            
            prefixSum += nums[i];
            maxSum = Math.max(maxSum, prefixSum - minSum);
            minSum = Math.min(minSum, prefixSum);
        }
        
        return maxSum;
        
        
        
    }
}