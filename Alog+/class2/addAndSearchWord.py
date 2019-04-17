class TrieNode:
    
    def __init__(self):
        
        self.children = {}
        self.isWord = False 

class WordDictionary:
    """
    @param: word: Adds a word into the data structure.
    @return: nothing
    """
    
    def __init__(self):
        
        self.root = TrieNode()
        
        
    def addWord(self, word):
        # write your code here
        
        node = self.root 
        
        for c in word:
            
            if c not in node.children:
                
                node.children[c] = TrieNode()
                
            node = node.children[c]
            
        node.isWord = True 
            
            

    """
    @param: word: A word could contain the dot character '.' to represent any one letter.
    @return: if the word is in the data structure.
    """
    def search(self, word):
        # write your code here
        
        if word is None:
            
            return False 
            
        return self.searchHelper(self.root, word, 0)
        
    def searchHelper(self, node, word, index):
        
        if node is None:
            
            return False 
            
        if index >= len(word):
            
            return node.isWord
            
        
        c = word[index]
        
        if c != '.':
            
            return self.searchHelper(node.children.get(c), word, index + 1)
            
        else:
            
            for child in node.children:
                
                if self.searchHelper(node.children[child], word, index + 1):
                    
                    return True 
                    
            return False 
            