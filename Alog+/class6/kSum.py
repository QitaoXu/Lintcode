class Solution:
    """
    @param A: An integer array
    @param k: A positive integer (k <= length(A))
    @param target: An integer
    @return: An integer
    """
    def kSum(self, A, k, target):
        
        n = len(A)
        
        f = [[[0 for _ in range(target + 1)] for _ in range(k + 1)] for _ in range(n + 1)]
        
        f[0][0][0] = 1 
        
        for i in range(1, n + 1):
            for j in range(0, k + 1):
                for t in range(target + 1):
                    
                    f[i][j][t] = f[i - 1][j][t]
                    
                    if j >= 1 and t >= A[i - 1]:
                        f[i][j][t] += f[i - 1][j - 1][t - A[i - 1]]
                        
        return f[n][k][target]

    """
    def __init__(self):
        self.result = 0
        
    def kSum(self, A, k, target):
        # write your code here
        
        nums = A 
        
        if nums is None or len(nums) == 0:
            
            return self.result
        
        self.kSumHelper(nums, [], 0, k, target, {})
        
        return self.result
        
    def kSumHelper(self, nums, combination, start_index, k, target, memo):
        
        if target == 0 and k == 0:
            self.result += 1 
            return 
        
        
        for i in range(start_index, len(nums)):
            
            if nums[i] > target:
                break 
            
            combination.append(nums[i])
            
            self.kSumHelper(nums, combination, i + 1, k - 1, target - nums[i], memo)
            
            combination.pop()
            
    """