class Solution:
    """
    @param pattern: a string, denote pattern string
    @param teststr: a string, denote matching string
    @return: an boolean, denote whether the pattern string and the matching string match or not
    """
    def wordPattern(self, pattern, teststr):
        # write your code here
        
        words = teststr.split()
        
        patterns = pattern 
        
        if len(words) != len(patterns):
            
            return False 
            
        pattern_to_word, word_to_pattern = {}, {} 
        
        for pattern, word in zip(patterns, words):
            
            if pattern in pattern_to_word and pattern_to_word[pattern] != word:
                
                return False 
                
            pattern_to_word[pattern] = word 
            
            if word in word_to_pattern and word_to_pattern[word] != pattern:
                
                return False 
                
            word_to_pattern[word] = pattern 
            
        return True 