# Given a set of distinct integers, return all possible subsets.

class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsetHelper(self, nums, subset, startIndex, results):
        
        results.append(subset.copy())
        
        for i in range(startIndex, len(nums)):
            subset.append(nums[i])
            self.subsetHelper(nums, subset, i + 1, results)
            subset.pop()
        
    
    def subsets(self, nums):
        # write your code here
        results = []
        if nums == None:
            return results
        
        
        nums.sort()
        subset = []
        self.subsetHelper(nums, subset, 0, results)
        
        return results