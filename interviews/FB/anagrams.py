class Solution:
    """
    @param strs: A list of strings
    @return: A list of strings
    """
    def anagrams(self, strs):
        # write your code here
        
        hashMap = {}
        
        result = []
        
        for s in strs:
            
            std = ''.join(sorted(s))
            
            if std not in hashMap:
                
                hashMap[std] = []
                
            hashMap[std].append(s)
            
        for std in hashMap:
            
            if len(hashMap[std]) > 1:
                
                result += hashMap[std]
                
        return result