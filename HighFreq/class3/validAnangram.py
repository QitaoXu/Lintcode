class Solution:
    """
    @param s: The first string
    @param t: The second string
    @return: true or false
    """
    def anagram(self, s, t):
        # write your code here
        set_s = [0] * 256 
        set_t = [0] * 256 
        
        for c in t:
            
            set_t[ord(c)] += 1 
            
        for c in s:
            
            set_s[ord(c)] += 1 
            
        for i in range(256):
            
            if set_s[i] != set_t[i]:
                
                return False 
                
        return True 