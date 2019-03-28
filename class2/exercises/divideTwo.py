class Solution:
    """
    @param dividend: the dividend
    @param divisor: the divisor
    @return: the result
    """
    def divide(self, dividend, divisor):
        # write your code here
        INT_MAX = 2**31 - 1 
        
        if divisor == 0:
            
            return INT_MAX
            
        neg = dividend < 0 and divisor > 0 or dividend > 0 and divisor < 0
        
        dividend = abs(dividend)
        
        divisor = abs(divisor)
        
        ans, shift = 0, 31 
        
        while shift >= 0:
            
            if dividend >= divisor << shift:
                
                dividend -= divisor << shift
                
                ans += 1 << shift 
                
            shift -= 1 
            
        if neg:
            
            ans = -ans 
            
        if ans > INT_MAX:
            
            return INT_MAX
            
        return ans 