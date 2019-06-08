class TrieNode:

    def __init__(self):
        self.children = {} 
        self.isWord = False 

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def add(self, word):

        node = self.root 

        for c in word:

            if c not in node.children:
                node.children[c] = TrieNode()

            node = node.children[c]

    def find(self, word):

        node = self.root 

        for c in word:

            if c not in node.children:
                return None 

            node = node.children[c]

        return node 

    def search(self, word):

        node = self.find(word)

        return node is not None and node.isWord == True 

    def startsWith(self, prefix):

        node = self.find(prefix)

        return node is not None 

