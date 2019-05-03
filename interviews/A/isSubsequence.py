class Solution:
    """
    @param s: the given string s
    @param t: the given string t
    @return: check if s is subsequence of t
    """
    def isSubsequence(self, s, t):
        # Write your code here
        
        i, j = 0, 0 
        
        
        while i < len(s) and j < len(t):
            
            if s[i] == t[j]:
                
                i += 1 
                j += 1 
                
            else:
                
                j += 1 
                
        if i == len(s):
            return True 
            
        else:
            return False 