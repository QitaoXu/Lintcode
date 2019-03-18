from heapq import heappop, heappush

class Solution:
    """
    @param n: An integer
    @return: return a  integer as description.
    """
    def nthUglyNumber(self, n):
        # write your code here
        
        heap = [1]
        
        visited = set([1])
        
        val = None 
        
        for i in range(n):
            
            val = heappop(heap)
            
            for multi in [2, 3, 5]:
                
                if multi * val not in visited:
                    
                    visited.add(multi * val)
                    heappush(heap, multi * val)
                    
        return val
        