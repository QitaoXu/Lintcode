class Solution:
    """
    @param x: the given number x
    @param y: the given number y
    @param z: the given number z
    @return: whether it is possible to measure exactly z litres using these two jugs
    """
    def canMeasureWater(self, x, y, z):
        # Write your code here
        
        if x + y < z:
            
            return False 
            
        return z % self.gcd(x, y) == 0
        
    def gcd(self, x, y):
        
        if y == 0:
            
            return x 
            
        return self.gcd(y, x % y)
