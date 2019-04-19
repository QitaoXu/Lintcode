class Solution:
    """
    @param n: a number
    @return: Gray code
    """
    def grayCode(self, n):
        # write your code here
        return [i ^ (i >> 1) for i in range(1 << n)]
