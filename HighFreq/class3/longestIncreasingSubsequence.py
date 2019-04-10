class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        # write your code here
        if not nums:
            
            return 0
        
        dp = [1] * len(nums)
        
        for curt, val in enumerate(nums):
            
            for prev in range(curt):
                
                if nums[prev] < val:
                    
                    dp[curt] = max(dp[curt], dp[prev] + 1)
                    
        return max(dp)