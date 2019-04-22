class TrieNode:
    
    def __init__(self):
        
        self.children = {}
        self.isWord = False 
        
class Trie:
    
    def __init__(self):
        # do intialization if necessary
        self.root = TrieNode()
        

    """
    @param: word: a word
    @return: nothing
    """
    def insert(self, word):
        # write your code here
        
        node = self.root 
        
        for c in word:
            
            if c not in node.children:
                
                node.children[c] = TrieNode()
                
            node = node.children[c]
            
        node.isWord = True 
        
    def find(self, word):
        
        node = self.root
        
        for c in word:
            
            if c not in node.children:
                
                return None 
                
            node = node.children[c]
            
        return node 

    """
    @param: word: A string
    @return: if the word is in the trie.
    """
    def search(self, word):
        # write your code here
        node = self.find(word)
        
        return node is not None and node.isWord

    """
    @param: prefix: A string
    @return: if there is any word in the trie that starts with the given prefix.
    """
    def startsWith(self, prefix):
        # write your code here
        
        node = self.find(prefix)
        
        return node is not None
    
class Solution:
    def findAllConcatenatedWordsInADict(self, words):
        
        if not words:
            
            return [] 
        
        prefixTree = Trie()
        
        results = []
        
        for word in words:
            
            prefixTree.insert(word)
            
        for word in words:
            
            if self.dfs(word, 0, [], prefixTree):
                
                results.append(word) 
                
        return results
        
        
    def dfs(self, string, start_index, combination, prefixTree):
        
        if start_index == len(string):
            
            return True if len(combination) > 1 else False
        
        for i in range(start_index, len(string)):
            
            prefix = string[start_index : i + 1]
            
            if not prefixTree.search(prefix):
                
                continue 
                
            combination.append(prefix)
                
            if self.dfs(string, i + 1, combination, prefixTree):
                
                return True 
            
            combination.pop()
            
        return False 
            
            
        
        