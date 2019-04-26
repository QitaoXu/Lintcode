from heapq import heappush, heappop

DIRECTION = [(0, 1), (1, 0)]

class Solution:
    """
    @param matrix: a matrix of integers
    @param k: An integer
    @return: the kth smallest number in the matrix
    """
    def kthSmallest(self, matrix, k):
        # write your code here
        
        m, n = len(matrix), len(matrix[0])
        
        if m * n < k:
            
            return matrix[m - 1][n - 1]
        
        visited = set()
        
        heap = [] 
        
        heappush(heap, (matrix[0][0], 0, 0) )
        
        visited.add((0, 0))
        
        for _ in range(k - 1):
            
            val, x, y = heappop(heap)
            
            for dx, dy in DIRECTION:
                
                nx, ny = x + dx, y + dy 
                
                if not self.is_valid(nx, ny, matrix):
                    
                    continue 
                
                if (nx, ny) in visited:
                    
                    continue 
                
                heappush(heap, (matrix[nx][ny], nx, ny))
                
                visited.add((nx, ny))
                
        val, x, y = heappop(heap)
        
        return val 
        
    def is_valid(self, x, y, matrix):
        
        if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
            
            return False 
            
        return True 
            
