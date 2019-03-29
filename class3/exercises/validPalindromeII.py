class Solution:
    """
    @param s: a string
    @return: nothing
    """
    def validPalindrome(self, s):
        # Write your code here
        
        start, end = 0, len(s) - 1 
        
        while start < end:
            
            if s[start] != s[end]:
                if s[start + 1] != s[end] and s[start] != s[end - 1]:
                    return False 
                    
            start += 1 
            end -= 1 
            
        return True