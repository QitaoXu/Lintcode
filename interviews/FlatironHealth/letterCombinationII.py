MAPPING = {
    "2" : ("a", "b", "c"),
    "3" : ("d", "e", "f"),
    "4" : ("g", "h", "i"),
    "5" : ("j", "k", "l"),
    "6" : ("m", "n", "o"),
    "7" : ("p", "q", "r", "s"),
    "8" : ("t", "u", "v"),
    "9" : ("w", "x", "y", "z") 
}

class TrieNode:

    def __init__(self):

        self.children = {} 
        self.isWord = False 

class Trie:

    def __init__(self):
        self.root = TrieNode() 

    def insert(self, word):

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

    def search(self, word):

        node = self.find(word) 

        return node != None and node.isWord == True 

    def startsWith(self, prefix):

        node = self.find(prefix)

        return node != None 

class Solution:
    def letterCombinations(self, digits, dictionary):
        
        results = [] 
        
        if not digits:
            return results 

        prefixTree = Trie()

        for word in dictionary:

            prefixTree.insert(word) 
        
        string = ""
        index = 0 
        
        self.dfs(digits, string, index, prefixTree, results)
        
        return results 
    
    def dfs(self, digits, string, index, prefixTree, results):
        
        if index == len(digits):
            
            results.append(string[:]) 
            
            return 
        
        for letter in MAPPING[digits[index]]:

            if not prefixTree.startsWith(string + letter):
                continue 
            
            self.dfs(digits, string + letter, index + 1, prefixTree, results)
            
        
        
        