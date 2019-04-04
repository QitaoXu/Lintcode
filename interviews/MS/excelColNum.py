class Solution:
    """
    @param n: a integer
    @return: return a string
    """
    def convertToTitle(self, n):
        # write your code here
        
        digits = self.n_to_digits(n)
        
        res = ""
        
        for digit in digits:
            
            res = res + chr(digit + ord('A'))
            
        return res 
    
    def n_to_digits(self, n):
        
        digits = [] 
        
        while n > 0:
            
            n -= 1 
            
            digit = n % 26
            
            digits.append(digit)
            
            n = n // 26 
        
        digits.reverse()
        
        return digits