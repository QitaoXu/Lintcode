class Solution:
    """
    @param n: The number of queens.
    @return: The total number of distinct solutions.
    """
    def totalNQueens(self, n):
        # write your code here
         
        boards = [] 
        
        permutation = [] 
        
        visited = {
                    "col" : set(),
                    "sum" : set(),
                    "diff" : set()
        }
        
        self.dfs(n, permutation, visited, boards)
        
        return len(boards)
        
    def dfs(self, n, permutation, visited, boards):
        
        if len(permutation) == n:
            
            boards.append(permutation.copy())
            
            return 
        
        row = len(permutation)
        
        for col in range(n):
            
            if not self.is_valid(permutation, col, visited):
                continue 
            
            permutation.append(col)
            visited["col"].add(col)
            visited['sum'].add(row + col)
            visited['diff'].add(row - col)
            
            self.dfs(n, permutation, visited, boards)
            
            visited['col'].remove(col)
            visited['sum'].remove(row + col)
            visited['diff'].remove(row - col)
            permutation.pop() 
            
            
            
    def is_valid(self, permutation, col, visited):
        
        row = len(permutation)
        
        if col in visited['col']:
            return False 
            
        if row + col in visited['sum']:
            return False 
            
        if row - col in visited['diff']:
            return False 
            
        return True 