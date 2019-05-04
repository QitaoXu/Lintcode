class Solution:
    """
    @param s: a string
    @param excludewords: a dict
    @return: the most frequent word
    """
    def frequentWord(self, s, excludewords):
        # Write your code here
        
        s = s.lower() + "."
        
        word_to_count = {}
        max_count = 0 
        max_word = ""
        
        word = ""
        
        for c in s:
            
            if c.isalpha():
                word += c 
                
            elif len(word) > 0:
                
                if word not in excludewords:
                    
                    word_to_count[word] = word_to_count.get(word, 0) + 1 
                    
                    if word_to_count[word] > max_count:
                        max_word = word
                        max_count = word_to_count[word]
                        
                    if word_to_count[word] == max_count:
                        if word < max_word:
                            max_word = word 
                            
                word = ""
                
        return max_word