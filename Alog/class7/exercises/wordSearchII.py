DIRECTIONS = [
    (-1, 0), (0, -1), (1, 0), (0, 1)
]

class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """
    def wordSearchII(self, board, words):
        # write your code here
        
        
        words_set = set(words)
        
        prefix_set = set()
        
        for word in words:
            for i in range(len(word)):
                prefix_set.add(word[:i + 1])
                
        results = set()
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                visited = set([(i, j)])
                self.dfs(board, i, j, board[i][j], words_set, prefix_set, visited, results)
                
        return list(results)
        
    def dfs(self, board, x, y, word, words_set, prefix_set, visited, results):
        
        if word in words_set:
            results.add(word)
        
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            
            if not self.inside(nx, ny, board):
                continue
            
            if (nx, ny) in visited:
                continue 
            
            if word + board[nx][ny] not in prefix_set:
                continue 
            
            visited.add((nx, ny))
            
            self.dfs(board, nx, ny, word + board[nx][ny], words_set, prefix_set, visited, results)
            
            visited.remove((nx, ny))
            
    def inside(self, x, y, board):
        
        row, col = len(board), len(board[0])
        
        return 0 <= x < row and 0 <= y < col
            
                
