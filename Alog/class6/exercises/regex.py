class Solution:
    """
    @param s: A string 
    @param p: A string includes "." and "*"
    @return: A boolean
    """
    def isMatch(self, s, p):
        # write your code here
        return self.isMatchHelper(s, 0, p, 0, {})
    
    def isMatchHelper(self, source, i, pattern, j, memo):
        
        if (i, j) in memo:
            return memo[(i, j)]
            
        if len(source) == i:
            
            return self.is_empty(pattern[j:])
            
        if len(pattern) == j:
            return False 
            
        if j + 1 < len(pattern) and pattern[j + 1] == '*':
            matched = self.is_match_char(source[i], pattern[j]) and self.isMatchHelper(source, i + 1, pattern, j, memo) or \
                        self.isMatchHelper(source, i, pattern, j + 2, memo)
        else:
            matched = self.is_match_char(source[i], pattern[j]) and \
                        self.isMatchHelper(source, i + 1, pattern, j + 1, memo)
                        
        memo[(i, j)] = matched
        
        return matched 
        
    def is_match_char(self, s, p):
        return s == p or p == '.'
        
    def is_empty(self, pattern):
        
        if len(pattern) % 2 == 1:
            return False 
            
        for i in range(len(pattern) // 2):
            
            if pattern[i * 2 + 1] != '*':
                return False 
                
        return True 
        
        
        
        