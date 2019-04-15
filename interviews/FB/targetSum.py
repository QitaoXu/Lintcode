class Solution:
    """
    @param nums: the given array
    @param s: the given target
    @return: the number of ways to assign symbols to make sum of integers equal to target S
    """
    def findTargetSumWays(self, nums, s):
        # Write your code here
        
        return self.dfs(nums, 0, 0, s, {})
        
        
    def dfs(self, nums, index, addup, target, memo):
        
        if (index, addup) in memo:
            
            return memo[(index, addup)]
            
        if index == len(nums):
                
            memo[(index, addup)] = 1 if addup == target else 0 
            
            return memo[(index, addup)]
                
            
        count = 0 
                
        count += self.dfs(nums, index + 1, addup + nums[index], target, memo)
                
        count += self.dfs(nums, index + 1, addup - nums[index], target, memo)
            
        memo[(index, addup)] = count 
        
        return count 
        