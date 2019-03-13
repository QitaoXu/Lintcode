class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        # write your code here
        
        visited = {
                    "col" : set(),
                    "diff" : set(),
                    "sum" : set()
                    }
        results = [] 
        
        permutation = [] 
        
        self.dfs(n, permutation, visited, results)
        
        return results
        
        
    def dfs(self, n, permutation, visited, results):
        
        if len(permutation) == n:
            results.append(self.draw(permutation))
            return 
        
        row = len(permutation)
        
        for col in range(n):
            
            if not self.is_valid(permutation, visited, col):
                continue 
            
            permutation.append(col)
            visited['col'].add(col)
            visited['diff'].add(row - col)
            visited['sum'].add(row + col)
            
            self.dfs(n, permutation, visited, results)
            
            visited['col'].remove(col)
            visited['diff'].remove(row - col)
            visited['sum'].remove(row + col)
            permutation.pop()
            
    def is_valid(self, permutation, visited, col):
        
        row = len(permutation)
        
        if col in visited['col']:
            return False 
            
        if row - col in visited['diff']:
            return False 
            
        if row + col in visited['sum']:
            return False 
            
        return True 
        
    
    
    def draw(self, permutation):
        
        board = [] 
        
        n = len(permutation)
        
        for col in permutation:
            
            row_string = ''.join([ 'Q' if c == col else '.' for c in range(n)])
            board.append(row_string)
            
        return board