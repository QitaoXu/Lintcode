class Solution:
    def reverseWords(self, s: str) -> str:
        
        if not s:
            return s 
        
        words = s.split()
        
        words.reverse()
        
        return " ".join(words)