class Solution:
    def mostCommonWord(self, paragraph, banned):
        banset = set(banned)
        word_to_count = {}
        
        max_word = ""
        max_count = 0 
        word = ""
        paragraph += '.'
        result = set()
        
        for c in paragraph.lower():
            
            if c.isalpha():
                word = word + c 
                
            elif len(word) > 0:
                if word not in banset:
                    word_to_count[word] = word_to_count.get(word, 0) + 1 
                    
                    if word_to_count[word] > max_count:
                        max_count = word_to_count[word]
                        max_word = word 
                        result.clear()
                        result.add(word)
                        
                    if word_to_count[word] == max_count:
                        result.add(word) 
                            
                word = ""
                
        return max_word, list(result)

solution = Solution() 
string = "Bob Bob Alan Alan Ser Claire Claire"
banned = ["bob"]

print(solution.mostCommonWord(string, banned))