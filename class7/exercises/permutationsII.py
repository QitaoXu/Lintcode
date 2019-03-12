class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums):
        # write your code here
        results = [] 
        if nums is None:
            return results 
            
        permutation = [] 
        # visited = [False for _ in range(len(nums))] 
        visited = [False] * len(nums) 
        
        nums.sort()
        
        self.dfs(nums, visited, permutation, results)
        
        return results
        
    def dfs(self, nums, visited, permutation, results):
        
        if len(permutation) == len(nums):
            results.append(permutation.copy())
            return 
        
        for i in range(0, len(nums)):
            
            if visited[i] == True:
                continue 
            
            if i > 0 and nums[i] == nums[i - 1] and visited[i - 1] == False:
                continue 
            
            permutation.append(nums[i])
            visited[i] = True 
            
            self.dfs(nums, visited, permutation, results)
            
            visited[i] = False 
            permutation.pop() 