class Solution:
    """
    @param nums: the gievn integers
    @return: the total Hamming distance between all pairs of the given numbers
    """
    def totalHammingDistance(self, nums):
        # Write your code here
        
        total, n = 0, len(nums)
        
        for i in range(32):
            
            bit_count = 0 
            
            for j in range(n):
                
                bit_count += (nums[j] >> i) & 1 
                
            total += bit_count * (n - bit_count)
            
        return total
