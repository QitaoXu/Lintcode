class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """
    def strStr(self, source, target):
        # Write your code here
        if source == None or target == None:
            return -1
        
        n = len(source)
        m = len(target)
        
        for i in range(0, n - m + 1):
            j = 0
            while j < m:
                if source[i + j] != target[j]:
                    break
                j += 1
            if j == m:
                return i 
        return -1