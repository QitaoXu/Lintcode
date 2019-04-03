class Solution:
    """
    @param nums: an array
    @param k: a target value
    @return: the maximum length of a subarray that sums to k
    """
    def maxSubArrayLen(self, nums, k):
        # Write your code here
        
        prefix_sum_arr = [0]
        prefix_sum = 0
        
        prefixSum_plus_k_to_index = {}
        prefixSum_plus_k_to_index[k] = 0
        
        max_length = 0
        
        for i in range(0, len(nums)):
            
            prefix_sum += nums[i]
            
            prefix_sum_arr.append(prefix_sum)
            
            if prefix_sum in prefixSum_plus_k_to_index:
                
                max_length = max(max_length, i + 1 - prefixSum_plus_k_to_index[prefix_sum])
                
            if prefix_sum + k not in prefixSum_plus_k_to_index:
                
                prefixSum_plus_k_to_index[prefix_sum + k] = i + 1 
                
        return max_length
            
            
