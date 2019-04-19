import re 

class Solution:
    """
    @param paragraph: 
    @param banned: 
    @return: nothing
    """
    def mostCommonWord(self, paragraph, banned):
        
        if not paragraph:
            
            return None 
            
        banned_set = set(banned)
        
        word_to_count = {}
        
        words = re.findall(r'\w+', paragraph.lower())
        
        max_count = 0 
        max_word = ""
        
        for word in words:
            
            word = word.lower()
            
            if word in banned_set:
                
                continue 
            
            word_to_count[word] = word_to_count.get(word, 0) + 1 
            
            if word_to_count[word] > max_count:
                
                max_word = word
                max_count = word_to_count[word]
                
        return max_word