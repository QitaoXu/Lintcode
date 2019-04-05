class Solution:
    """
    @param n: a integer
    @return: return a integer
    """
    def trailingZeroes(self, n):
        # write your code here
        
        return  0 if n == 0 else n // 5 + self.trailingZeroes(n // 5)