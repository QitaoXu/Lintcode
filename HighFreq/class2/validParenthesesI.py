PAIR = {
    '(' : ')',
    '{' : '}',
    '[' : ']'
}


class Solution:
    """
    @param s: A string
    @return: whether the string is a valid parentheses
    """
    def isValidParentheses(self, s):
        # write your code here
        
        if s is None:
            
            return False 
            
        if len(s) == 0:
            
            return True 
        
        stack = [] 
        
        for c in s:
            
            if c == '(' or c == '[' or c == '{':
                
                stack.append(c)
                
            else:
                
                if len(stack) == 0: 
                    
                    return False 
                    
                elif stack and PAIR[stack[-1]] != c:
                    
                    return False
                    
                stack.pop()   
                
        return len(stack) == 0