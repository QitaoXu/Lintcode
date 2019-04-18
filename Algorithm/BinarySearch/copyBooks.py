class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """
    def copyBooks(self, pages, k):
        # write your code here
        
        if not pages:
            
            return 0 
            
        start = max(pages)
        end = sum(pages)
        
        while start + 1 < end:
            
            mid = start + (end - start) // 2 
            
            if self.can_complete(pages, k, mid):
                
                end = mid 
                
            else:
                
                start = mid 
                
        if self.can_complete(pages, k, start):
            
            return start 
            
        # Since even if there is only one person,
        # he or she can copy all books, just return end.
        return end 
        
    def can_complete(self, pages, k, tl):
        
        num = 1 
        
        pageSum = 0
        
        for page in pages:
            
            if pageSum + page <= tl:
                
                pageSum += page 
                
            else:
                
                num += 1 
                pageSum = page 
                
        return num <= k 