class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def singleNumber(self, A):
        # write your code here
        ans = 0
        
        for x in A:
            
            ans = ans ^ x
            
        return ans