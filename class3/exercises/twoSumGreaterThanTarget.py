class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: an integer
    """
    def twoSum2(self, nums, target):
        # write your code here
        if nums == None or len(nums) == 0:
            return 0
            
        i, j = 0, len(nums) - 1 
        
        nums.sort()
        count = 0
        
        while i < j:
            
            if nums[i] + nums[j] > target:
                count += j - i  
                j -= 1 
                
            else:
                i += 1 
                
        return count 
                