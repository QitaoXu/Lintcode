class Solution:
    """
    @param s: a string
    @return: an integer
    """
    def lengthOfLongestSubstring(self, s):
        # write your code here
        
        left, right = 0, 0 
        
        longest = 0 
        
        unique_char = set()
        
        while left < len(s):
            
            while right < len(s) and s[right] not in unique_char:
                
                unique_char.add(s[right])
                
                right += 1 
                
            longest = max(longest, right - left)
            
            unique_char.remove(s[left])
            
            left += 1 
            
        return longest