class Solution:
    """
    @param dict: an array of n distinct non-empty strings
    @return: an array of minimal possible abbreviations for every word
    """
    def wordsAbbreviation(self, dict):
        # write your code here
        if not dict:
            
            return []
        
        wordDict = dict 
        abbr_to_times = {}
        n = len(wordDict)
        prefix_length = [1] * n 
        ans = [] 
        
        for i in range(n):
            
            abbr = self.get_abbr(wordDict[i], prefix_length[i])
            
            ans.append(abbr)
            
            abbr_to_times[abbr] = abbr_to_times.get(abbr, 0) + 1 
            
        # unique = True
            
        while True:
            
            unique = True 
            
            for i in range(n):
                
                if abbr_to_times[ans[i]] > 1:
                    
                    prefix_length[i] += 1 
                    
                    new_abbr = self.get_abbr(wordDict[i], prefix_length[i])
                    
                    abbr_to_times[new_abbr] = abbr_to_times.get(new_abbr, 0) + 1 
                    ans[i] = new_abbr
                    
                    unique = False 
                    
            if unique:
                
                break 
            
        return ans    
        
    def get_abbr(self, word, prefix_len):
        
        if prefix_len >= len(word) - 2:
            
            return word 
            
        left = word[:prefix_len]
        
        right = word[-1]
        
        mid_count = len(word) - prefix_len - 1 # total - left - right 
        
        return left + str(mid_count) + right 