class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    # def permute(self, nums):
    #     # write your code here
    #     results = [] 
    #     if nums is None:
    #         return results 
            
    #     permutation = [] 
    #     visited = [False] * len(nums)
        
    #     self.dfs(nums, visited, permutation, results)
        
    #     return results
        
    # def dfs(self, nums, visited, permutation, results):
        
    #     if len(permutation) == len(nums):
    #         results.append(permutation.copy())
    #         return 
        
    #     for i in range(0, len(nums)):
            
    #         if visited[i] == True:
    #             continue 
            
    #         permutation.append(nums[i])
    #         visited[i] = True 
            
    #         self.dfs(nums, visited, permutation, results)
            
    #         visited[i] = False 
    #         permutation.pop() 
    
    def permute(self, A):
        A.sort()
        result = []

        hasNext = True  # hasNext 为 true 时，表示可以继续迭代
        while hasNext:
            current = list(A)  # 进行数组复制
            result.append(current)
            hasNext = self.nextPermutation(A)
        
        return result
            
            
    def nextPermutation(self, nums):
        # write your code here
        
        if len(nums) <= 1:
            return False
            
        i = len(nums) - 1 
        
        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1 
            
        if i <= 0:
            return False
            
        if i != 0:
            j = len(nums) - 1 
            
            while nums[j] <= nums[i - 1]:
                j -= 1 
                
            nums[i - 1], nums[j] = nums[j], nums[i - 1]
            
        self.swapList(nums, i, len(nums) - 1)
        
        return True
        # return nums
        
    def swapList(self, nums, i, j):
        
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1 
            j -= 1 
        