class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        return self.isMatchHelper(s, 0, p, 0, {})
        
    def isMatchHelper(self, s, i, p, j, memo):
        
        if (i, j) in memo:
            
            return memo[(i, j)]
        
        if len(s) == i:
            
            for index in range(j, len(p)):
                
                if p[index] != '*':
                    
                    return False 
                
            return True 
        
        if len(p) == j:
            
            return False 
        
        if p[j] != '*':
            
            matched = self.is_match_char(s[i], p[j]) and \
                        self.isMatchHelper(s, i + 1, p, j + 1, memo)
            
        else:
            
            matched = self.isMatchHelper(s, i + 1, p, j, memo) or \
                        self.isMatchHelper(s, i, p, j + 1, memo)
            
        memo[(i, j)] = matched 
        
        return matched 
    
    def is_match_char(self, s, p):
        
        return s == p or p == '?'
        
        