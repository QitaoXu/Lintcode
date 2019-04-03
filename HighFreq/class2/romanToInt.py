convert = {
    '0' : 0, 
    'I' : 1,
    'V' : 5,
    'X' : 10,
    'L' : 50,
    'C' : 100,
    'D' : 500,
    'M' : 1000
}
class Solution:
    """
    @param s: Roman representation
    @return: an integer
    """
    def romanToInt(self, s):
        # write your code here
        
        s += '0'
        
        ans = 0 
        
        for i in range(0, len(s) - 1):
            
            if convert[s[i]] < convert[s[i + 1]]:
                
                ans -= convert[s[i]]
                
            else:
                
                ans += convert[s[i]]
                
        return ans 
        
        
