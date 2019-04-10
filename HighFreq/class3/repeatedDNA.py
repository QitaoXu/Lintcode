class Solution:
    """
    @param s: a string represent DNA sequences
    @return: all the 10-letter-long sequences 
    """
    def findRepeatedDna(self, s):
        # write your code here
        
        sequences_to_times = {} 
        
        results = set()
        
        for window_start in range(0, len(s) - 9):
            
            window_end = window_start + 9
            
            window_word = s[window_start : window_end + 1]
            
            sequences_to_times[window_word] = sequences_to_times.get(window_word, 0) + 1 
            
            if sequences_to_times[window_word] > 1:
                
                results.add(window_word)
                
        return list(results)
        
        
