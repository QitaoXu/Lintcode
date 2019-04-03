class Solution:
    """
    @param tokens: The Reverse Polish Notation
    @return: the value
    """
    def evalRPN(self, tokens):
        # write your code here
        
        stack = [] 
        
        for token in tokens:
            
            if not self.is_operator(token):
                
                stack.append(self.token_to_num(token))
                
            else:
                
                op1 = stack.pop()
                op2 = stack.pop()
                
                if token == '+':
                    
                    stack.append(op2 + op1)
                    
                elif token == '-':
                    
                    stack.append(op2 - op1)
                    
                elif token == '*':
                    
                    stack.append(op2 * op1)
                    
                else:
                    
                    stack.append(int(op2 * 1.0 / op1))
                    
        return stack[0]
        
    def is_operator(self, token):
        
        if token == '+' or token == '-' or token == '*' or token == '/':
            
            return True 
            
        return False 
        
    def token_to_num(self, token):
        
        return int(token)