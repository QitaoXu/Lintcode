import re 
class Solution:
    """
    @param s: a string
    @param excludewords: a dict
    @return: the most frequent word
    """
    def frequentWord(self, s, excludewords):
        # Write your code here
        
        s = " " + s 
        
        word_list = re.findall(r"\b\S+\b", s)
        
        ans = {} 
        max_count = 0 
        max_word = ""
        
        for word in word_list:
            if word not in excludewords:
                
                ans[word] = ans.get(word, 0) + 1 
                
                if ans[word] > max_count:
                    max_count = ans[word]
                    max_word = word 
                
                elif ans[word] == max_count:
                    if word < max_word:
                        max_word = word 
                        
        return max_word