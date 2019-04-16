from heapq import heappush, heappop

DIRECTION = [(0, 1), (1, 0)]

class Solution:
    """
    @param A: an integer arrays sorted in ascending order
    @param B: an integer arrays sorted in ascending order
    @param k: An integer
    @return: An integer
    """
    def kthSmallestSum(self, A, B, k):
        # write your code here
        
        m = len(A)
        n = len(B)
        
        if m * n < k:
            
            return A[-1] + B[-1]
            
        heap = [] 
        
        visited = set()
        
        heappush(heap, (A[0] + B[0], 0, 0))
        visited.add((0, 0))
        
        for _ in range(k - 1):
            
            val, x, y = heappop(heap)
            
            for dx, dy in DIRECTION:
                
                nx, ny = x + dx, y + dy 
                
                if not self.is_valid(nx, ny, m, n):
                    
                    continue 
                
                if (nx, ny) in visited:
                    
                    continue 
                
                heappush(heap, (A[nx] + B[ny], nx, ny))
                visited.add((nx, ny))
                
        val, x, y = heappop(heap)
        
        return val 
        
    def is_valid(self, x, y, m, n):
        
        if x < 0 or x >= m or y < 0 or y >= n:
            
            return False 
            
        return True 