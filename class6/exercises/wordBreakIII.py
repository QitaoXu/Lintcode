class Solution:
    """
    @param: : A string
    @param: : A set of word
    @return: the number of possible sentences.
    """

    def wordBreak3(self, s, dict):
        # Write your code here
        
        results = [] 
        
        if s is None:
            return 0 
            
        combination = [] 
        
        memo = {}
        
        lower_dict = set()
        
        for word in dict:
            
            lower_dict.add(word.lower())
        
        partitions = self.wordBreakHelper(s.lower(), combination, lower_dict, results, memo)
        
        return partitions
        
        
        
    def wordBreakHelper(self, s, combination, wordDict, results, memo):
        
        if s in memo:
            return memo[s]
            
        if len(s) == 0:
            return 0
            
        partitions = 0 
        
        for i in range(1, len(s) + 1):
            
            prefix = s[:i]
            
            if prefix not in wordDict:
                continue 
            
            combination.append(prefix)
            
            sub_partitions = self.wordBreakHelper(s[i:], combination, wordDict, results, memo)

            partitions += sub_partitions
                
            combination.pop()
            
            
        if s in wordDict:
            partitions += 1 
        
        memo[s] = partitions
        
        return partitions