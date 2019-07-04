class Solution:
    def evalRPN(self, tokens):
        
        stack = [] 
        op_set = set(['+', '-', '*', '/'])
        
        for token in tokens:
            
            if token not in op_set:
                
                stack.append(int(token)) 
                
            else: 
                
                op2 = stack.pop()
                op1 = stack.pop() 
                
                if token == '+': 
                    stack.append(op1 + op2) 
                    
                elif token == '-':
                    stack.append(op1 - op2)
                    
                elif token == '*':
                    stack.append(op1 * op2) 
                    
                else:
                    stack.append(int(op1 / op2)) 
                    
        return stack[-1] 
                
            
                
                
                
        