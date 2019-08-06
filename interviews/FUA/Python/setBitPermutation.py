class SetBits:

    BitsSetTable = [0 for _ in range(256)] 

    for i in range(256):
        BitsSetTable[i] = (i & 1) + BitsSetTable[i // 2] 

    @classmethod
    def lookUp(self, num):

        return SetBits.BitsSetTable[num & 0xFF] +\
            SetBits.BitsSetTable[(num >> 8) & 0xFF] +\
            SetBits.BitsSetTable[(num >> 16) & 0xFF] +\
            SetBits.BitsSetTable[(num >> 24) & 0xFF] 

class Solution:

    def findAllSetBitPermutationNum(self, num):

        setBitNum = SetBits.lookUp(num) 

        return self.setBitPermutation(setBitNum) 

    def setBitPermutation(self, setBitNum):

        results = [] 

        if setBitNum < 0 or setBitNum > 32:
            return results 

        self.dfs(setBitNum, 0, [], results) 

        return results
        

    def dfs(self, setBitNum, index, permutation, results):

        if setBitNum == 0:

            permutation = permutation[::-1] 
            results.append(self.bitsToNum(permutation))
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

print(solution.findAllSetBitPermutationNum(8))    