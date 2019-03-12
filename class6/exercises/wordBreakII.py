class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """
    def wordBreak(self, s, wordDict):
        # write your code here
        results = []
        if not s:
            return results
        
        combination = [] 
        
        memo = {}
        
        results = self.wordBreakHelper(s, combination, wordDict, memo)
        
        return results
        
        
    def wordBreakHelper(self, s, combination, wordDict, memo):
        
        
        if s in memo:
            return memo[s]
            
        if len(s) == 0:
            return []
        
        partitions = []
        
        for i in range(len(s)):
            
            prefix = s[:i + 1]
            
            if prefix not in wordDict:
                continue 
            
            combination.append(prefix)
            
            sub_partitions = self.wordBreakHelper(s[i + 1:], combination, wordDict, memo)
            
            for sub_partition in sub_partitions:
                
                partitions.append(prefix + " " + sub_partition)
                
            combination.pop()
            
        if s in wordDict:
            partitions.append(s)
            
        memo[s] = partitions
            
        return partitions