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
            
            for successor in self.get_successors(s, dict):
                
                if successor not in seen:
                    
                    if len(successor) < min_length:
                        min_length = len(successor)
                        
                    queue.append(successor)
                    seen.add(successor)
                    
        return min_length            
        
    def get_successors(self, s, dict):
            
        successors = []
            
        for sub in dict:
                
            found = s.find(sub)
                
            while found != -1:
                    
                successor = s[: found] + s[found + len(sub) :]
                
                successors.append(successor)
                
                found = s.find(sub, found + 1)
                
        return successors
            
            
        
        
            
            