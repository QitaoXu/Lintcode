class Solution:
    """
    @param s: an expression includes numbers, letters and brackets
    @return: a string
    """
    def expressionExpand(self, s):
        # write your code here
        
        stack = [] 
        
        for c in s:
            
            if c != ']':
                
                stack.append(c)
                
                continue 
            
            strs = [] 
            
            while stack and stack[-1] != '[':
                
                strs.append(stack.pop())
                
            stack.pop()
            
            num = 0 
            base = 1
            
            while stack and stack[-1].isdigit():
                
                num += int(stack.pop()) * base 
                
                base *= 10 
                
            stack.append( "".join(reversed(strs)) * num )
            
        return "".join(stack)
                