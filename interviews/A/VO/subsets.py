class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    
    def subsets(self, nums):
        # write your code here
        results = [] 
        
        if nums is None:
            
            return results 
            
        nums.sort()
        
        combination = [] 
        
        self.susbsetsHelper(nums, combination, 0, results)
        
        return results
        
    def susbsetsHelper(self, nums, combination, start_index, results):
        
        results.append(combination.copy())
        
        for i in range(start_index, len(nums)):
            
            combination.append(nums[i])
            self.susbsetsHelper(nums, combination, i + 1, results)
            combination.pop()