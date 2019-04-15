import sys
class Solution:
    """
    @param: A: An integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def continuousSubarraySum(self, A):
        # write your code here
        
        
        left = 0 
        
        addup = 0 
        
        res = [-1, -1]
        
        max_sum = -sys.maxsize 
        
        for right in range(len(A)):
            
            if addup < 0:
                
                addup = A[right]
                
                left = right 
                
            else:
                
                addup += A[right]
                
            if addup > max_sum:
                
                max_sum = addup
                
                res[0] = left
                
                res[1] = right 
                
        return res 