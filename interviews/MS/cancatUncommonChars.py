class Solution:
    """
    @param s1: the 1st string
    @param s2: the 2nd string
    @return: uncommon characters of given strings
    """
    def concatenetedString(self, s1, s2):
        # write your code here
        ans = [] 
        
        for c in s1:
            
            if c not in s2:
                
                ans.append(c)
                
        for c in s2:
            
            if c not in s1:
                
                ans.append(c)
                
        return "".join(ans)
