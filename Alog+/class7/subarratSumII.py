class Solution:
    """
    @param A: An integer array
    @param start: An integer
    @param end: An integer
    @return: the number of possible answer
    """
    def subarraySumII(self, A, start, end):
        # write your code here
        
        if not A:
            return 0 
            
        n = len(A)
        
        prefix_sum = [0]
        
        for i in range(0, n):
            prefix_sum.append(prefix_sum[-1] + A[i])
            
        l, r = 0, 0 
        
        res = 0 
        
        for i in range(1, n + 1):
            
            while l < i and prefix_sum[i] - prefix_sum[l] > end:
                l += 1 
                
            while r < i and prefix_sum[i] - prefix_sum[r] >= start:
                r += 1 
                
            res += r - l 
            
        return res 