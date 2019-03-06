from collections import deque 

class Solution:
    """
    @param: s: a string
    @param: dict: a set of n substrings
    @return: the minimum length
    """
    def minLength(self, s, dict):
        # write your code here
        
        queue = deque() 
        seen = set() 
        
        queue.append(s)
        seen.add(s)
        
        min_length = len(s)
        
        while queue:
            
            s = queue.popleft() 
            
            for sub in dict:
                
                found = s.find(sub)
                
                while found != -1:
                    
                    new_s = s[: found] + s[found + len(sub):]
                    
                    if new_s not in seen:
                        if len(new_s) < min_length:
                            min_length = len(new_s)
                            
                        queue.append(new_s)
                        seen.add(new_s)
                        
                    found = s.find(sub, found + 1)
        return min_length