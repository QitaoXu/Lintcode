class SuffixTrieNode:

    def __init__(self):

        self.children = {} 

    def insertSuffix(self, string):

        if len(string) > 0:

            c = string[0] 

            if c not in self.children:
                self.children[c] = SuffixTrieNode() 

            self.children[c].insertSuffix(string[1:]) 

class SuffixTrie:

    def __init__(self, string):

        self.root = SuffixTrieNode() 

        for i in range(len(string)):

            self.root.insertSuffix(string[i:]) 

    def countNodes(self):

        return self.countNodesHelper(self.root) 

    def countNodesHelper(self, node):

        # if node is None:
        #     return 0 

        count = 0 

        for c in node.children:
            count += self.countNodesHelper(node.children[c]) 

        return 1 + count 

string = "ab" 

suffixTrie = SuffixTrie(string)

print(suffixTrie.countNodes()) 

    