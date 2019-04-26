import collections 
"""
Definition of TrieNode:
class TrieNode:
    def __init__(self):
        # <key, value>: <Character, TrieNode>
        self.children = collections.OrderedDict()
        self.top10 = []
"""
class TrieNode:
    def __init__(self):
        # <key, value>: <Character, TrieNode>
        self.children = collections.OrderedDict()
        self.top10 = []

class TrieService:

    def __init__(self):
        self.root = TrieNode()

    def get_root(self):
        # Return root of trie root, and 
        # lintcode will print the tree struct.
        return self.root

    # @param {str} word a string
    # @param {int} frequency an integer
    # @return nothing
    def insert(self, word, frequency):
        # Write your your code here
        node = self.get_root()
        
        for c in word:
            
            if c not in node.children:
                node.children[c] = TrieNode()
                
            self.add_frequency(node.children[c].top10, frequency)
                
            node = node.children[c]
            
    def add_frequency(self, top10, frequency):
        
        top10.append(frequency)
        index = len(top10) - 1 
        
        while index > 0:
            if top10[index] > top10[index - 1]:
                top10[index], top10[index - 1] = top10[index - 1], top10[index]
                index -= 1 
                
            else:
                break 
        
        if len(top10) > 10:
            top10.pop()
        
        
        
       


