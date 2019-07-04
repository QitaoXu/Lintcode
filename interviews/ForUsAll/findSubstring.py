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

    def findAllSubstring(self, word):

        n = len(word) 

        prefixTree = Trie() 
        substrings = []

        for i in range(n): 
            for j in range(i + 1, n + 1): 

                substring = word[i:j] 

                if prefixTree.search(substring):
                    continue 

                prefixTree.insert(substring) 
                substrings.append(substring) 

        return substrings 


solution = Solution() 
word = "abcbc" 

print(solution.findAllSubstring(word))