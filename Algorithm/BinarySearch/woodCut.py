class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def woodCut(self, L, k):
        # write your code here
        if not L:
            
            return 0 
        
        start, end = 1, max(L)
        
        while start + 1 < end:
            
            mid = start + (end - start) // 2 
            
            if self.get_pieces(L, mid) >= k:
                
                start = mid 
                
            else:
                
                end = mid 
                
        if self.get_pieces(L, end) >= k:
            
            return end 
            
        if self.get_pieces(L, start) >= k:
            
            return start 
            
        return 0 
        
    # Compute how many pieces can be generated at most 
    # if the length of each piece is fixed        
    def get_pieces(self, L, length):
        
        num = 0 
        
        for l in L:
            
            num += l // length
            
        return num 
