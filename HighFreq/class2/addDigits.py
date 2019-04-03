class Solution:
    """
    @param num: a non-negative integer
    @return: one digit
    """
    def addDigits(self, num):
        # write your code here
        
        if num == 0:
            
            return 0
        
        digits = self.num_to_digits(num)
        
        while len(digits) > 1:
            
            num = sum(digits)
            
            digits = self.num_to_digits(num)
            
        return digits[0]
        
    def num_to_digits(self, num):
        
        digits = [] 
        
        while num > 0:
            
            digit = num % 10
            
            digits.append(digit)
            
            num = num // 10 
            
        digits.reverse()
        
        return digits 