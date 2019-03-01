class Solution:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    """
    def twoSum5(self, nums, target):
        # write your code here
        
        if nums == None or len(nums) == 0:
            return 0 
            
        start, end = 0, len(nums) - 1
        
        nums.sort()
        count = 0
        
        while start < end:
            
            if nums[start] + nums[end] > target:
                end -= 1 
                
            else:
                count += end - start
                start += 1 
                
        return count 