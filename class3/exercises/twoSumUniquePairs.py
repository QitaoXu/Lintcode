class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def twoSum6(self, nums, target):
        # write your code here
        if nums == None or len(nums) == 0:
            return 0 
            
        start, end = 0, len(nums) - 1 
        
        # nums = [(num, i) for i, num in enumerate(nums)]
        
        # nums = sorted(nums, key = lambda x:x[0])
        nums.sort()
        count = 0
        results = []
        
        while start < end: 
            
            if nums[start] + nums[end] < target:
                start += 1 
                
            if nums[start] + nums[end] == target:
                count, start, end = count + 1, start + 1, end - 1 
                while start < end and nums[end] == nums[end + 1]:
                    end -= 1 
                while start < end and nums[start] == nums[start - 1]:
                    start += 1 
                
            if nums[start] + nums[end] > target:
                end -= 1 
                
        return count