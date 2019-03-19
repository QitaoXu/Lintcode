class Solution:
    """
    @param: nums: a list of integers
    @return: A integer indicate the sum of minimum subarray
    """
    def minSubArray(self, nums):
        # write your code here
        
        min_sum, max_sum = sys.maxsize, 0 
        
        prefix_sum = 0 
        
        for num in nums:
            
            prefix_sum += num 
            
            min_sum = min(min_sum, prefix_sum - max_sum)
            
            max_sum = max(max_sum, prefix_sum)
            
        return min_sum