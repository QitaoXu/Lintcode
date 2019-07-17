class Solution:

    def setBitPermutation(self, setBitNum):

        results = [] 

        if setBitNum < 0 or setBitNum > 32:
            return results 

        self.dfs(setBitNum, 0, [], results) 

        return results
        

    def dfs(self, setBitNum, index, permutation, results):

        if setBitNum == 0:

            permutation = permutation[::-1] 
            results.append(self.bitsToNum(permutation.copy())) 
            return 

        if index == 32 or 32 - index < setBitNum:
            return 

        permutation.append(0) 
        self.dfs(setBitNum, index + 1, permutation, results) 
        permutation.pop() 

        permutation.append(1)  
        self.dfs(setBitNum - 1, index + 1, permutation, results) 
        permutation.pop() 

    def bitsToNum(self, bits):

        num = 0 

        for bit in bits:

            num = num * 2 + bit 

        return num 

solution = Solution() 

print(solution.setBitPermutation(32))   