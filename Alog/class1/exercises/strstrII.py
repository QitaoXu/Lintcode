# Implement strStr function in O(n + m) time.

# strStr return the first index of the target string in a source string. 
# The length of the target string is m and the length of the source string is n.
# If target does not exist in source, just return -1.

class Solution:
    """
    @param: source: A source string
    @param: target: A target string
    @return: An integer as index
    """
    def strStr2(self, source, target):
        # write your code here
        if target == None or source == None:
            return -1
        
        if len(target) == 0:
            return 0
        
        m = len(target)
        BASE = 1000000
        power = 1 
        for i in range(0, m):
            power = power * 31 % BASE
        
        targetCode = 0 
        for i in range(0, m):
            targetCode = (targetCode * 31 + ord(target[i])) % BASE
        
        hashCode = 0
            
        for i in range(0, len(source)):
            hashCode = (hashCode * 31 + ord(source[i])) % BASE
            
            if i < m:
                continue
            
            if i >= m:
                hashCode = (hashCode - power * ord(source[i - m])) % BASE
                if hashCode < 0:
                    hashCode += BASE
                if hashCode == targetCode:
                    if target == source[i - m + 1 : i + 1]:
                        return i - m + 1 
            
            
        return -1
