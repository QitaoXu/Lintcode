class Solution:
    """
    @param n: An integer
    @return: true if this is a happy number or false
    """
    def isHappy(self, n):
        # write your code here
        
        if n == 0:
            
            return False 
            
        square_set = set()
        
        while n != 1:
            
            digits = self.num_to_digits(n)
            
            n = self.digits_to_square_sum(digits)
            
            if n in square_set:
                
                return False 
                
            square_set.add(n)
            
        return True 
    
    
    def num_to_digits(self, n):
        
        results = [] 
        
        while n > 0:
            
            digit = n % 10 
            
            results.append(digit)
            
            n = n // 10 
            
        results.reverse()
        
        return results
        
    def digits_to_square_sum(self, digits):
        
        square_sum = 0 
        
        for digit in digits:
            
            square_sum += digit ** 2 
            
        return square_sum