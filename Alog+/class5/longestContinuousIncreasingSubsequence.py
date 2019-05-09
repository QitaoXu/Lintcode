class Solution:
    """
    @param A: An array of Integer
    @return: an integer
    """
    def longestIncreasingContinuousSubsequence(self, A):
        # write your code here
        
        if not A:
            return 0 
            
        n = len(A)
        length = 1 
        ans = 1 
        for i in range(1, n):
            
            if A[i] > A[i - 1]:
                length += 1 
                
            else:
                length = 1 
            
            ans = max(ans, length)
        
        length = 1 
        for i in range(n - 2, -1, -1):
            
            if A[i] > A[i + 1]:
                length += 1 
                
            else:
                length = 1 
                
            ans = max(ans, length)
        
        return ans 