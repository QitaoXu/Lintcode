class Solution:
    """
    @param s: a string
    @return: it's index
    """
    def firstUniqChar(self, s):
        # write your code here
        
        alp_to_times = {} 
        
        for c in s:
            
            if c not in alp_to_times:
                
                alp_to_times[c] = 1 
                
            else:
                
                alp_to_times[c] += 1 
                
        for i in range(len(s)):
            
            if alp_to_times[s[i]] == 1:
                
                return i 
                
        return -1 