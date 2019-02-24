class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s):
        if not s:
            return ""
        
        n = len(s)

        is_Palindrome = [ [False] * n for _ in range(n) ]
        for i in range(n):
            is_Palindrome[i][i] = True
        for i in range(1, n):
            is_Palindrome[i][i - 1] = True

        longest, start, end = 1, 0, 0

        for length in range(1, n):
            for i in range(0, n - length):
                j = i + length
                is_Palindrome[i][j] = ( s[i] == s[j] and is_Palindrome[i + 1][j - 1] )
                if is_Palindrome[i][j] and (length + 1) > longest:
                    longest = length + 1
                    start, end = i, j 

        return s[start : end + 1]