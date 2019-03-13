class Solution:
    """
    @param pattern: a string,denote pattern string
    @param str: a string, denote matching string
    @return: a boolean
    """
    def wordPatternMatch(self, pattern, str):
        # write your code here
        
        return self.is_match(pattern, str, {}, set())
    
    def is_match(self, pattern, string, mapping, used):
        
        if not pattern:
            return not string 
            
        char = pattern[0]
        
        if char in mapping:
            
            word = mapping[char]
            
            if not string.startswith(word):
                return False
                
            else:
                return self.is_match(pattern[1:], string[len(word):], mapping, used)
                
        for i in range(len(string)):
            
            word = string[:i + 1]
            
            if word in used:
                continue 
            
            mapping[char] = word 
            used.add(word)
            
            if self.is_match(pattern[1:], string[len(word):], mapping, used):
                return True
            
            del mapping[char]
            used.remove(word)
            
        return False