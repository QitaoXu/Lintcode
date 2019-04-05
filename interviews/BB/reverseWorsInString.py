class Solution:
    """
    @param: s: A string
    @return: A string
    """
    def reverseWords(self, s):
        # write your code here
        
        if not s:
            
            return s 
            
        words = s.split()
        
        words.reverse()
        
        return " ".join(words)