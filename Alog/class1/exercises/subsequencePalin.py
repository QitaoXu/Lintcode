class Solution(object):
    """
    @param s: the maximum length of s is 1000
    @return: the longest palindromic subsequence's length
    """
    def longestPalindromeSubseq(self, s):
        # write your code here
        if not s:
            return 0 
            
            results = []
            subsequence = ""
            self.subsequenceHelper(s, subsequence, 0, results)
            # print(results)
            longest = 1
            
            for sub in results:
                if self.isPalindrome(sub):
                    if len(sub) > longest:
                        longest = len(sub)
                        
            return longest
    
    def subsequenceHelper(self, s, subsequence, startIndex, results):
        results.add(subsequence.copy()) # deep copy
        
        for i in range(startIndex, len(s)):
            subsequence = subsequence + s[startIndex]
            self.subsequenceHelper(s, subsequence, i + 1, results)
            subsequence = subsequence[0 : len(subsequence) - 1 ]
            
        
    def isPalindrome(self, s):
        if s == None:
            return False 
            
        if len(s) == 0 or len(s) == 1:
            return True
        
        start, end = 0, len(s) - 1 
        while start < end:
            if s[start] != s[end] and start < end:
                return False 
            start += 1 
            end -= 1
            
        return True

solution = Solution()
solution.longestPalindromeSubseq("aaaaba")
