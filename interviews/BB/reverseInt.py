class Solution:
    """
    @param n: the integer to be reversed
    @return: the reversed integer
    """
    def reverseInteger(self, n):
        # write your code here
        
        if n == 0:
            
            return 0 
            
        max_num = 2**31 - 1 
        min_num  = -2 ** 31
        
        is_negative = False 
        
        digits = []
        
        if n < 0:
            
            is_negative = True 
            
            digits = self.num_to_digits(-n)
            
        else:
            
            digits = self.num_to_digits(n)

            
        res = self.digits_to_num(digits)
        
        if is_negative:
            
            return -res if -res > min_num else 0 
            
        else:
            
            return res if res < max_num else 0
        
    def num_to_digits(self, n):
        
        digits = [] 
        
        while n > 0:
            
            digit = n % 10 
            
            digits.append(digit)
            
            n = n // 10 
            
        return digits
        
    def digits_to_num(self, digits):
        
        n = 0 
        
        for digit in digits:
            
            n = n * 10 + digit 
            
        return n 
