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
            
            return  match_str
            
        
        target_hash = self.get_hash(target)
        target_length = len(target_hash)
        
        
        match_hash = {} 
        match_length = 0 
        
        left, right = 0, 0 
        
        mini_length = len(source) + 1
        
        n = len(source)
        
        for left in range(n):
            
            while right < n and match_length < target_length:
                
                char = source[right]
                
                if char in target_hash:
                    
                    match_hash[char] = match_hash.get(char, 0) + 1 
                    
                    if match_hash[char] == target_hash[char]:
                        
                        match_length += 1 
                        
                right += 1 
                
            
            # compare mini_length and current (right - left) when target_length == match_length
            if right - left < mini_length and target_length == match_length:
                
                mini_length = right - left 
                match_str = source[left : right]
                
            char = source[left]
            
            if char in target_hash:
                
                if target_hash[char] == match_hash[char]:
                    
                    match_length -= 1 
                    
                match_hash[char] -= 1 
                
        return match_str
                
        
    def get_hash(self, target):
        
        hash_set = {} 
        
        for char in target:
            
            hash_set[char] = hash_set.get(char, 0) + 1 
            
        return hash_set
                    