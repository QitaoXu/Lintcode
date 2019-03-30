class Solution:
    """
    @param nums: an array of Integer
    @param target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, nums, target):
        # write your code here
        if nums == None or len(nums) == 0:
            return None 
            
        start, end = 0, len(nums) - 1 
        
        while start < end: 
            if nums[start] + nums[end] < target:
                start += 1 
                
            if nums[start] + nums[end] == target:
                break 
            
            if nums[start] + nums[end] > target:
                end -= 1 
                
        if nums[start] + nums[end] == target:
            if start < end:
                return [start + 1, end + 1]
                
            else:
                return [end + 1, start + 1]