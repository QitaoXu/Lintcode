class Solution:
    """
    @param s: a string
    @param t: a string
    @return: true if the characters in s can be replaced to get t or false
    """
    def isIsomorphic(self, s, t):
        # write your code here
        
        map1 = {}
        map2 = {}
        
        for i in range(len(s)):
            
            if s[i] not in map1:
                map1[s[i]] = t[i]
                
            elif map1[s[i]] != t[i]:
                return False 
                
        for i in range(len(t)):
            
            if t[i] not in map2:
                map2[t[i]] = s[i]
                
            elif map2[t[i]] != s[i]:
                return False 
                
        return True 
