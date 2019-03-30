import math
class Solution:
    """
    @param n: An integer
    @return: a list of combination
    """
    def getFactors(self, n):
        # write your code here
        results = [] 
        combination = [] 
        
        self.getFactorHelper(n, combination, 2, results)
        
        return results
        
    def getFactorHelper(self, n, combination, start_factor, results):
        
        if n <= 1:
            if len(combination) > 1:
                results.append(combination.copy())
            # results.append(combination.copy())
            return 
        
        for i in range(start_factor, int(math.sqrt(n)) + 1):
            if n % i == 0:
                combination.append(i)
                self.getFactorHelper(n // i, combination, i, results)
                combination.pop() 

        combination.append(n)
        self.getFactorHelper(1, combination, n, results)
        combination.pop()