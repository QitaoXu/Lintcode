class Solution:
    """
    @param A: an integer array sorted in ascending order
    @param target: An integer
    @return: an integer
    """
    def closestNumber(self, A, target):
        # write your code here
        if not A:
            
            return -1 
            
        nums = A
            
        start, end = 0, len(nums) - 1 
        
        while start + 1 < end:
            
            mid = (start + end) // 2 
            
            if nums[mid] < target:
                
                start = mid 
                
            elif nums[mid] == target:
                
                return mid 
                
            else:
                
                end = mid 
                
        return start if abs(nums[start] - target) <= abs(nums[end] - target) else end 