class Solution:
    def subarraySum(self, nums, k):
        
        count = 0 
        prefix_sum = 0
        prefix_sum_to_times = {0: 1}
        
        for num in nums:
            
            prefix_sum += num 
            
            if prefix_sum - k in prefix_sum_to_times:
                
                count += prefix_sum_to_times[prefix_sum - k]
                
            if prefix_sum in prefix_sum_to_times:
                
                prefix_sum_to_times[prefix_sum] += 1 
                
            else:
                
                prefix_sum_to_times[prefix_sum] = 1 
            
        return count 
        
        
            
            