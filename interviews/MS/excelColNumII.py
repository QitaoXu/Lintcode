class Solution:
    """
    @param s: a string
    @return: return a integer
    """
    def titleToNumber(self, s):
        # write your code here
        
        digits = self.s_to_digits(s)
        
        num = self.digits_to_num(digits)
        
        return num
        
        
    def s_to_digits(self, s):
        
        digits = [] 
        
        for c in s:
            
            digit = ord(c) - ord('A') + 1
            
            digits.append(digit)
            
        return digits
        
    def digits_to_num(self, digits):
        
        num = 0 
        
        for digit in digits:
            
            num = num * 26 + digit 
            
        return num 
        
        
