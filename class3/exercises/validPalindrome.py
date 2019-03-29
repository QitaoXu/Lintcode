class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome(self, s):
        # write your code here
        start, end = 0, len(s) - 1 
        
        while start < end: 
            
            while start < end and not s[start].isalpha() and not s[start].isdigit():
                start += 1 
                
            while start < end and not s[end].isalpha() and not s[end].isdigit():
                end -= 1 
                
            if s[start].lower() != s[end].lower():
                return False 
                
            start += 1 
            end -= 1 
            
        return True 