class Solution:
    """
    @param: words: a set of words without duplicates
    @return: all word squares
    """
    def wordSquares(self, words):
        # write your code here
        
        if not words or not words[0]:
            
            return [] 
            
        results = [] 
        
        prefix_to_words = {} 
        
        self.initPrefix(words, prefix_to_words)
        
        path = [] 
        
        self.dfs(0, len(words[0]), prefix_to_words, path, results)
        
        return results 
        
    def initPrefix(self, words, prefix_to_words):
        
        prefix_to_words[""] = set()
        
        for word in words:
            
            prefix_to_words[""].add(word)
            
            for i in range(1, len(word) + 1):
                
                prefix = word[:i]
                
                if prefix not in prefix_to_words:
                    
                    prefix_to_words[prefix] = set()
                    
                prefix_to_words[prefix].add(word)
                
    def dfs(self, l, wordLength, prefix_to_words, path, results):
        
        if l == wordLength:
            
            results.append(path.copy())
            
            return 
        
        
        prefix = ""
        
        for i in range(0, l):
            
            prefix += path[i][l]
            
        for word in prefix_to_words[prefix]:
            
            if not self.checkPrefix(l, word, wordLength, prefix_to_words, path):
                
                continue 
            
            path.append(word)
            
            self.dfs(l + 1, wordLength, prefix_to_words, path, results)
            
            path.pop()
            
    def checkPrefix(self, l, next_word, wordLength, prefix_to_words, path):
        
        for j in range(l + 1, wordLength):
            
            prefix = ""
            
            for i in range(0, l):
                
                prefix += path[i][j]
                
            prefix += next_word[j]
            
            if prefix not in prefix_to_words:
                
                return False 
                
        return True 