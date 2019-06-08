DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

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

class Solution:
    def findWords(self, board, words):
        
        grid = board 
        
        m, n = len(grid), len(grid[0])
        
        results = set()
        
        prefixTree = Trie()
        
        for word in words:
            
            prefixTree.add(word)
            
        for i in range(m):
            for j in range(n):
                
                if prefixTree.startsWith(grid[i][j]):
                    
                    visited = set()
                    visited.add((i, j))
                    
                    self.dfs(grid, i, j, [grid[i][j]], visited, prefixTree, results)
                    
        return list(results)
    
    def dfs(self, grid, x, y, permutation, visited, prefixTree, results):
        
        if prefixTree.search("".join(permutation)):
            results.add("".join(permutation))
            
        for dx, dy in DIRECTIONS:
            
            nx, ny = x + dx, y + dy 
            
            if not self.isValid(grid, nx, ny):
                continue 
                
            if (nx, ny) in visited:
                continue 
                
            if not prefixTree.startsWith("".join(permutation + [grid[nx][ny]])):
                continue 
                
            permutation.append(grid[nx][ny])
            visited.add((nx, ny))
            
            self.dfs(grid, nx, ny, permutation, visited, prefixTree, results)
            
            visited.remove((nx, ny))
            permutation.pop()
            
    def isValid(self, grid, x, y):
        
        m, n = len(grid), len(grid[0])
        
        if x < 0 or x >= m or y < 0 or y >= n:
            return False 
        
        return True 
            