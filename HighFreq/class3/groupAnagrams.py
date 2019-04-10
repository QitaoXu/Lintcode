class Solution:
    """
    @param strs: the given array of strings
    @return: The anagrams which have been divided into groups
    """
    def groupAnagrams(self, strs):
        # write your code here
        if not strs:
            
            return strs
        
        anagram_dict = {} 
        
        for word in strs:
            
            sorted_word = "".join( sorted(list(word)) )
            
            if sorted_word not in anagram_dict:
                
                anagram_dict[sorted_word] = [word]
                
            else:
                
                anagram_dict[sorted_word].append(word)
                
        return anagram_dict.values()