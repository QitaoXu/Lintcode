DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

class TrieNode:

    def __init__(self):
        self.children = {} 
        self.isWord = False 

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def printTrie(self, root):

        if len(root.children) == 0:
            return  

        for child in root.children:
            print(child + " ")
            self.printTrie(root.children[child])
            

    def add(self, word):

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
        return node is not None and node.isWord == True 

    def startsWith(self, prefix):
        node = self.find(prefix)
        return node is not None 

class Solution:

    def outputPathString(self, words, grid):

        results = set()

        m, n = len(grid), len(grid[0])

        prefixTree = Trie()

        for word in words:
            prefixTree.add(word)

        # prefixTree.printTrie(prefixTree.root)

        for i in range(m):
            for j in range(n):

                if not prefixTree.startsWith(grid[i][j]):
                    continue 

                visited = set()
                visited.add((i, j))

                self.dfs(grid, i, j, [grid[i][j]], prefixTree, results, visited)

        return list(results) 

    def dfs(self, grid, x, y, permutation, prefixTree, results, visited):

        if prefixTree.search("".join(permutation)):
            # print(str(x) + " " + str(y) + " " + "".join(permutation))

            results.add("".join(permutation.copy()))
            

        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy 

            if not self.isValid(grid, nx, ny):
                continue 

            if (nx, ny) in visited:
                continue 

            if not prefixTree.startsWith("".join(permutation) + grid[nx][ny]):
                continue 

            permutation.append(grid[nx][ny])
            visited.add((nx, ny))

            self.dfs(grid, nx, ny, permutation, prefixTree, results, visited)

            visited.remove((nx, ny))
            permutation.pop()

    def isValid(self, grid, x, y):

        m, n = len(grid), len(grid[0])

        if x < 0 or x >= m or y < 0 or y >= n:
            return False 

        return True 

            

solution = Solution()

grid = [["a", "b", "c", "d"],
        ["x", "y", "o", "t"],
        ["d", "o", "t", "a"],
        ["a", "b", "c", "d"]]

words = ["dat", "cot", "clear", "cotcd"]

print(solution.outputPathString(words, grid))             