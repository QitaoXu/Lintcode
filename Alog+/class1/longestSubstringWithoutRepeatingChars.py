class Solution:
    """
    @param s: a string
    @return: an integer
    """
    def lengthOfLongestSubstring(self, s):
        # write your code here
        
        i, j = 0, 0 
        
        longest = 0 
        
        unique_char = set()
        
        while i < len(s):
            
            while j < len(s) and s[j] not in unique_char:
                
                unique_char.add(s[j])
                
                j += 1 
                
            longest = max(longest, j - i)
            
            unique_char.remove(s[i])
            
            i += 1 
            
        return longest
            