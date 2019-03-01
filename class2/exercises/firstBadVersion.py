#class SVNRepo:
#    @classmethod
#    def isBadVersion(cls, id)
#        # Run unit tests to check whether verison `id` is a bad version
#        # return true if unit tests passed else false.
# You can use SVNRepo.isBadVersion(10) to check whether version 10 is a 
# bad version.
class Solution:
    """
    @param n: An integer
    @return: An integer which is the first bad version.
    """
    def findFirstBadVersion(self, n):
        # write your code here
        if n == None:
            return 0 
            
        start, end = 1, n 
        
        while ( start + 1 ) < end:
            
            mid = ( start + end ) // 2  
            
            if SVNRepo.isBadVersion(mid) == False:
                start = mid 
            elif SVNRepo.isBadVersion(mid) == True:
                end = mid 
                
        if SVNRepo.isBadVersion(start) == True:
            return start
            
        if SVNRepo.isBadVersion(end) == True: 
            return end 
            
        return 0