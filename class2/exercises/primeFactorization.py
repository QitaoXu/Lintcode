import math 

class Solution:
    """
    @param num: An integer
    @return: an integer array
    """
    def primeFactorization(self, num):
        # write your code here
        results = [] 
        
        k = 2 
        
        up = int(math.sqrt(num))
        
        while k <= up:
            while num % k == 0 and num > 1:
                num = num // k 
                results.append(k)
            k += 1
            
        if num > 1:
            results.append(num)
        
        return results