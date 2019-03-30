class Solution:
    """
    @param: s: A string
    @return: A list of lists of string
    """
    def partition(self, s):
        # write your code here
        results = [] 
            
        path = [] 
        
        self.dfs(s, path, results)
        
        return results 

    def is_palindrome(self, s):
        return s == s[::-1]
    
    
    def dfs(self, s, path, results):
        
        if len(s) == 0:
            results.append(list(path))
            return 
        
        
        for i in range(1, len(s) + 1):
            
            prefix = s[:i]
            
            if self.is_palindrome(prefix):
                
                path.append(prefix)
                self.dfs(s[i:], path, results)
                path.pop()