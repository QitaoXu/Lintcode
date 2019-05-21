class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        # write your code here
        results = [] 
        
        if nums is None:
            return results 
            
        nums.sort() 
        
        combination = [] 
        
        self.subsetsHelper(nums, combination, 0, results)
        
        return results 
        
    def subsetsHelper(self, nums, combination, start_index, results):
        
        results.append(combination.copy())
        
        for i in range(start_index, len(nums)):
            
            if i > 0 and nums[i] == nums[i - 1] and i > start_index:
                continue 
            
            combination.append(nums[i])
            self.subsetsHelper(nums, combination, i + 1, results)
            combination.pop()