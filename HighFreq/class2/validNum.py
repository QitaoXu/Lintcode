class Solution:
    """
    @param s: the string that represents a number
    @return: whether the string is a valid number
    """
    def isNumber(self, s):
        # write your code here
            
        i = 0 
        
        s = s.strip() + " "
        
        if s[i] == '+' or s[i] == '-':
            
            i += 1 
            
        n_digit, n_point = 0, 0 
        
        while s[i].isdigit() or s[i] == '.':
            
            if i < len(s) and s[i].isdigit():
                
                n_digit += 1 
                
            if i < len(s) and s[i] == '.':
                
                n_point += 1 
                
            i += 1 
            
        if n_digit <= 0 or n_point > 1:
            
            return False  
            
        if s[i] == 'e':
            
            i += 1 
            
            if s[i] == '+' or s[i] == '-':
                
                i += 1 
                
            if i == len(s) - 1:
                
                return False 
                
            while i < len(s) - 1:
                
                if not s[i].isdigit():
                    
                    return False 
                    
                i += 1 
                
        return i == len(s) - 1 
        
        