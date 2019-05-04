class Solution:
    """
    @param source : A string
    @param target: A string
    @return: A string denote the minimum window, return "" if there is no such a string
    """
    def minWindow(self, source , target):
        # write your code here
        
        match_str = ""
        if not source:
            return match_str
        
        target_hash = self.get_hash(target)
        target_count = len(target_hash)
        
        match_hash = {}
        match_count = 0 
        
        i, j = 0, 0 
        n = len(source)
        min_length = len(source) + 1 
        
        for i in range(n):
            
            while j < n and match_count < target_count:
                
                c = source[j]
                
                if c in target_hash:
                    match_hash[c] = match_hash.get(c, 0) + 1 
                    
                    if match_hash[c] == target_hash[c]:
                        match_count += 1 
                        
                j += 1 
                    
            if j - i < min_length and target_count == match_count:
                min_length = j - i 
                match_str = source[i : j]
                
            c = source[i]
            
            if c in target_hash:
                
                if match_hash[c] == target_hash[c]:
                    match_count -= 1 
                
                match_hash[c] -= 1 
                
        return match_str
        
    def get_hash(self, target):
        
        target_hash = {} 
        
        for c in target:
            
            target_hash[c] = target_hash.get(c, 0) + 1 
            
        return target_hash