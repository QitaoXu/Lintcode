import sys 
class Solution:
    """
    @param nums: an array of integers
    @param s: An integer
    @return: an integer representing the minimum size of subarray
    """
    def minimumSize(self, nums, s):
        # write your code here
        
        ans = sys.maxsize 
        
        left = 0 
        
        addup = 0 
        
        for right in range(len(nums)):
            
            addup += nums[right]
            
            while addup >= s:
                
                ans = min(ans, right - left + 1)
                
                addup -= nums[left]
                
                left += 1 
                
        return ans if ans != sys.maxsize else -1 