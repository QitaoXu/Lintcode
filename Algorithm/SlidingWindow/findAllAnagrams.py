class Solution:
    """
    @param s: a string
    @param p: a string
    @return: a list of index
    """
    def findAnagrams(self, s, p):
        # write your code here
        
        source = s 
        target = p 
        
        result = [] 
        
        if len(target) > len(source):
            
            return result 
            
        source_hash = {} 
        target_hash = {} 
        
        for i in range(len(target)):
            
            target_hash[target[i]] = target_hash.get(target[i], 0) + 1 
            source_hash[source[i]] = source_hash.get(source[i], 0) + 1 
        
        if source_hash == target_hash:
            
            result.append(0)
            
        for window_start in range(1, len(source) - len(target) + 1):
            
            window_end = window_start + len(target) - 1 
            
            source_hash[source[window_end]] = source_hash.get(source[window_end], 0) + 1 
            source_hash[source[window_start - 1]] -= 1 
            
            if source_hash[source[window_start - 1]] == 0:
                
                del source_hash[source[window_start - 1]]
                
            if source_hash == target_hash:
                
                result.append(window_start)
                
        return result