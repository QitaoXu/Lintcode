class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
    def fastPower(self, a, b, n):
        # write your code here
        
        if n == None or a == None or b == None:
            return 0 
        
        return self.fastPowerHelper(a, b, n)
        
        # if n == 0:
        #     return 1 % b
        
        # if n < 0:
        #     n = -n 
        #     a = 1.0 / a 
        
        # ans = 1
        # base = a 
        
        # while n > 0: 
        #     if n % 2 == 1:
        #         ans = ( (ans % b) * base) % b
        #     base = (base * base) % b 
            
        #     n = n // 2 

        # return ans 
        
    def fastPowerHelper(self, a, b, n):
        
        if n == 1:
            return a % b 
            
        if n == 0:
            return 1 % b
            
        power = self.fastPowerHelper(a, b, n // 2)
        
        power = ( power * power ) % b 
        
        if n % 2 == 1: # for each recursion, n may be odd
        
            power = (power * (a % b)) % b
        
        return power