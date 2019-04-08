class ValidWordAbbr:
    """
    @param: dictionary: a list of words
    """
    def __init__(self, dictionary):
        # do intialization if necessary
        self.abbr_to_words = {} 
        
        for word in dictionary:
            
            abbr = self.word_to_abbr(word)
            
            if abbr not in self.abbr_to_words:
                
                self.abbr_to_words[abbr] = set()
                
            self.abbr_to_words[abbr].add(word)
            
            
    """
    @param: word: a string
    @return: true if its abbreviation is unique or false
    """
    def isUnique(self, word):
        # write your code here
        
        abbr = self.word_to_abbr(word)
        
        if abbr not in self.abbr_to_words:
            
            return True 
            
        else:
            
            for abbr_word in self.abbr_to_words[abbr]:
                
                if word != abbr_word:
                    
                    return False 
                    
            return True 
            
        
    def word_to_abbr(self, word):
        
        if len(word) <= 2:
            
            return word 
            
        num = len(word) - 2
        
        abbr = word[0] + str(num) + word[-1]
        
        return abbr 

# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param = obj.isUnique(word)