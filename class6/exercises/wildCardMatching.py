class Solution:
    """
    @param s: A string 
    @param p: A string includes "?" and "*"
    @return: is Match?
    """
    def isMatch(self, s, p):
        # write your code here
        return self.isMatchHelper(s, 0, p, 0, {})

    def isMatchHelper(self, source, i, pattern, j, memo):
        
        if (i, j) in memo:
            return memo[(i, j)]
            
        if len(source) == i:
            
            for index in range(j, len(pattern)):
                
                if pattern[index] != '*':
                    return False
                    
            return True
            
        if len(pattern) == j:
            return False 
            
        if pattern[j] != '*':
            matched = self.is_match_char(source[i], pattern[j]) and \
                    self.isMatchHelper(source, i + 1, pattern, j + 1, memo)
        else:
            matched = self.isMatchHelper(source, i + 1, pattern, j, memo) or \
                    self.isMatchHelper(source, i, pattern, j + 1, memo)
                    
        memo[(i, j)] = matched 
        
        return matched
        
    def is_match_char(self, s, p):
        
        return p == '?' or s == p 