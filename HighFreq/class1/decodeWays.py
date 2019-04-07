class Solution:
    """
    @param s: a string,  encoded message
    @return: an integer, the number of ways decoding
    """
    def numDecodings(self, s):
        # write your code here
        
        if not s:
            
            return 0
        
        return self.dfs(s, {})
        
    def dfs(self, s, memo):
        
        if s in memo:
            
            return memo[s]
            
        if len(s) == 0:
            
            return 1
        
        if s[0] == '0':
            
            return 0 
    
        result = self.dfs(s[1:], memo)
        
        if len(s) >= 2  and int(s[0 : 2]) <= 26:
            
            result += self.dfs(s[2:], memo)
            
        memo[s] = result 
        
        return result 