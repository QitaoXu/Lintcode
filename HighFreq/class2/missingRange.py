class Solution:
    """
    @param: nums: a sorted integer array
    @param: lower: An integer
    @param: upper: An integer
    @return: a list of its missing ranges
    """
    def findMissingRanges(self, nums, lower, upper):
        # write your code here
        res = []
        
        if not nums:
            
            return [self.helper(lower, upper)] 
            
        prev_point = lower - 1 
        
        for point in nums:
            
            if prev_point != point and prev_point + 1 != point:
                
                res.append(self.helper(prev_point + 1, point - 1))
                
            prev_point = point
            
        if nums[-1] < upper:
            
            res.append(self.helper(nums[-1] + 1, upper))
            
        return res 
    
    def helper(self, left_point, right_point):
        
        if left_point == right_point:
            
            return str(left_point)
            
        else:
            
            return str(left_point) + "->" + str(right_point)
            
    