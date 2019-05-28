class Solution:

    def gcd(self, a, b):

        if a < b:
            return self.gcdHelper(a, b)

        else:
            return self.gcdHelper(b, a)

    def gcdHelper(self, small, big):

        if big % small == 0:
            return small 

        return self.gcdHelper(big % small, small)