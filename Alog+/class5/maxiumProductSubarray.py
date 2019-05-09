class Solution:
    """
    @param nums: An array of integers
    @return: An integer
    """
    def maxProduct(self, nums):
        # write your code here
        
        n = len(nums)
        
        f = [0 for _ in range(n)]
        g = [0 for _ in range(n)]
        
        f[0] = nums[0]
        g[0] = nums[0]
        
        ans = f[0]
        
        for i in range(1, n):
            
            f[i] = max(f[i - 1] * nums[i], g[i - 1] * nums[i], nums[i])
            g[i] = min(f[i - 1] * nums[i], g[i - 1] * nums[i], nums[i])
            
            ans = max(f[i], ans)
            
        return ans 