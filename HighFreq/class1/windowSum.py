class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    def winSum(self, nums, k):
        # write your code here
        results = []
        if nums == None or len(nums) == 0:
            return results 
    
        ksum = 0  
        for i in range(0, k):
            ksum += nums[i]
            
        results.append(ksum)
            
        for i in range(0, len(nums)):
            
            j = i + k
            
            if j >= len(nums):
                break
            
            ksum += nums[j]
            ksum -= nums[i]
            
            results.append(ksum)
            
        return results