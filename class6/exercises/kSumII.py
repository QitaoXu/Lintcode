class Solution:
    """
    @param: A: an integer array
    @param: k: a postive integer <= length(A)
    @param: targer: an integer
    @return: A list of lists of integer
    """
    def kSumII(self, A, k, target):
        # write your code here
        
        nums = A 
        
        results = []
        
        if nums is None:
            
            return results 
            
        nums.sort()
        
        combination = [] 
        
        self.kSumHelper(nums, combination, 0, results, k, target)
        
        return results 
        
    def kSumHelper(self, nums, combination, start_index, results, k, target):
        
        if target == 0 and k == 0:
            results.append(combination.copy())
            return 
        
        for i in range(start_index, len(nums)):
            
            if nums[i] > target:
                break 
            
            if i > 0 and nums[i] == nums[i - 1] and i > start_index:
                continue 
            
            if k == 0:
                break
            
            combination.append(nums[i])
            
            self.kSumHelper(nums, combination, i + 1, results, k - 1, target - nums[i])
            
            combination.pop()