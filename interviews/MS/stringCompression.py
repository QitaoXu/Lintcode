class Solution:
    """
    @param originalString: a string
    @return: a compressed string
    """
    def compress(self, originalString):
        # write your code here
        
        string = originalString
        
        if len(string) == 0:
            
            return string 
            
        ans = [] 
        
        last = string[0]
        
        count = 1 
        
        for c in string[1:]:
            
            if c == last:
                
                count += 1 
                
            else:
                
                ans.append(last)
                ans.append("%s" % count)
                
                count = 1 
                last = c 
                
        ans.append(last)
        ans.append("%s" % count)
        
        if len(ans) < len(string):
            
            return "".join(ans)
            
        else:
            
            return string 