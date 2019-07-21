class Solution:
    def calculate(self, s):
        
        if not s:
            return 0 
        
        num = 0 
        sign = '+'
        stack = [] 
        length = len(s)
        
        for i in range(length):
            
            if s[i].isdigit():
                num = num * 10 + int(s[i])
                
            if (s[i].isdigit() == False and s[i] != ' ') or i == length - 1:
                
                if sign == '+':
                    stack.append(num)
                    
                if sign == '-':
                    stack.append(-num)
                    
                if sign == '*':
                    stack.append(stack.pop() * num) 
                    
                if sign == '/':
                    tmp = stack.pop()
                    if tmp // num < 0 and tmp % num != 0:
                        stack.append(tmp // num + 1)
                    else:
                        stack.append(tmp // num)
                    
                sign = s[i]
                num = 0 
                
        res = 0
        
        for n in stack:
            res += n 
            
        return res 
        