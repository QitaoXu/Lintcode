class Solution:
    """
    @param nums: a binary array
    @return: the maximum length of a contiguous subarray
    """
    def findMaxLength(self, nums):
        # Write your code here
        
        prefix_sum, prefix_sum_to_index, longest = 0, {0 : 0}, 0 
        
        for i, num in enumerate(nums):
            
            prefix_sum += num if num == 1 else -1 
            
            if prefix_sum in prefix_sum_to_index:
                
                longest = max(longest, i + 1 - prefix_sum_to_index[prefix_sum])
                
            else:
                
                prefix_sum_to_index[prefix_sum] = i + 1 
                
        return longest