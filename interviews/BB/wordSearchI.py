from collections import deque

DIRECTION = [(0, 1), (1, 0), (0, -1), (-1, 0)]

class Solution:
    """
    @param board: A list of lists of character
    @param word: A string
    @return: A boolean
    """
    def exist(self, board, word):
        # write your code here
        
        
        if not board or len(board[0]) == 0:
            
            return False 
            
        if len(word) == 0:
            
            return True 
            
        visited = [ [False for j in range(len(board[0]))] for i in range(len(board)) ]
        
        for i in range(len(board)):
            
            for j in range(len(board[0])):
                
                if self.dfs(word, i, j, visited, board):
                    
                    return True 
                    
        return False 
        
        
    def dfs(self, word, i, j, visited, board):
        
        if len(word) == 0:
            
            return True 
            
        if not self.is_valid(i, j, board):
            
            return False 
            
        if board[i][j] == word[0] and not visited[i][j]:
            
            visited[i][j] = True 
            
            for di, dj in DIRECTION:
                
                ni, nj = i + di, j + dj 
                
                if self.dfs(word[1:], ni, nj, visited, board):
                    
                    return True 
                    
            visited[i][j] = False 
            
        return False 
        
    
            
    def is_valid(self, x, y, board):
        
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
            
            return False 
            
        return True 