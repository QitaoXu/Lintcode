class Solution:
    """
    @param nums: An array of integers
    @return: An integer
    """
    def findMissing(self, nums):
        # write your code here
        offset = nums[0]
                
        start, end = 0, len(nums) - 1 
        
        while start + 1 < end:
            
            mid = start + (end - start) // 2 
            
            if nums[mid] - offset > mid:
                
                end = mid 
                
            else:
                
                start = mid 
                
        if nums[start] - offset > start:
            return nums[start] - 1
        
        if nums[end] - offset > end:   
            return nums[end] - 1
            
        return nums[-1] + 1  

solution = Solution()

nums = [0, 1, 3]

print(solution.findMissing(nums))