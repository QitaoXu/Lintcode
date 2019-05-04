class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s):
        # write your code here
        
        if not s:
            return ""
            
        n = len(s)
            
        is_palindrome = [ [False for _ in range(n)] for _ in range(n) ]
        
        for i in range(n):
            is_palindrome[i][i] = True 
            
        for i in range(1, n):
            is_palindrome[i][i - 1] = True 
            
        start, end, longest = 0, 0, 1 
        
        for diff in range(1, n):
            for i in range(0, n - diff):
                j = i + diff 
                
                is_palindrome[i][j] = s[i] == s[j] and is_palindrome[i + 1][j - 1]
                if is_palindrome[i][j] and (diff + 1) > longest:
                    longest = (diff + 1)
                    start, end = i, j 
                    
        return s[start : end + 1]