class Solution:
    """
    @param s: the expression string
    @return: the answer
    """
    def __init__(self):
        self.i = 0 
        
    def calculate(self, s):
        # Write your code here
        
        return self.parseExp(s)
        
    def parseExp(self, s):
        
        nums = [] 
        op = '+'
        
        while self.i < len(s) and op != ')':
            
            if s[self.i] == ' ':
                self.i += 1 
                continue 
            
            if s[self.i] == '(':
                self.i += 1 
                n = self.parseExp(s)
                
            else:
                n = self.parseNum(s)
                
            if op == '+':
                nums.append(n)
                
            elif op == '-':
                nums.append(-n)
                
            elif op == '*':
                nums[-1] *= n 
                
            elif op == '/':
                nums[-1] //= n 
                
            if self.i >= len(s):
                break 
            
            op = s[self.i]
            
            self.i += 1 
            
        res = 0 
        for n in nums:
            res += n 
            
        return res 
        
    def parseNum(self, s):
        n = 0 
        
        while self.i < len(s) and s[self.i].isdigit():
            n = n * 10 + ord(s[self.i]) - ord('0')
            
            self.i += 1 
            
        return n 