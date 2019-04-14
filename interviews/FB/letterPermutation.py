class Solution:
    """
    @param S: a string
    @return: return a list of strings
    """
    def letterCasePermutation(self, S):
        # write your code here
        
        results = [] 
        
        if S is None:
            
            return results
        
        self.dfs(S, 0, results)
        
        return results 
        
    def dfs(self, s, start_index, results):
        
        results.append(s)
        
        for i in range(start_index, len(s)):
            
            if s[i].isdigit():
                
                continue 
            
            else:
                
                self.dfs(s[: i] + self.toggle(s[i]) + s[i + 1:], i + 1, results)
    
    def toggle(self, c):
        
        return c.upper() if c.islower() else c.lower()