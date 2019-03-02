class Solution:
    """
    @param x {float}: the base number
    @param n {int}: the power number
    @return {float}: the result
    """
    def myPow(self, x, n):
        # write your code here
        if n == 0:
            return 1 
            
        if n < 0:
            n = -n 
            x = 1.0 / x 
            
        return self.fastPowHelper(x, n)
        
        # ans = 1
        # base = x 
        # while n > 0: 
        #     if n % 2 == 1:
        #         ans = ans * base 
                
        #     base *= base 
        #     n // =2 
            
        # return ans
        
    def fastPowHelper(self, a, n):
        if n == 0:
            return 1
        
        if n == 1:
            return a 
            
        power = self.fastPowHelper(a, n // 2)
        
        power = power * power 
        
        if n % 2 == 1:
            power = power * a 
            
        return power 