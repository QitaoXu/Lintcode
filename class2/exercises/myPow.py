class Solution:
    """
    @param x {float}: the base number
    @param n {int}: the power number
    @return {float}: the result
    """
    def myPow(self, x, n):
        if n == 0:
            return 1 

        if n < 0:
            n = -n
            x = 1.0 / x 

        base = x
        ans = 1 
        while n > 0:
            if n % 2 == 1:
                ans = ans * base 

            base *= base
            n = n // 2 

        return ans


