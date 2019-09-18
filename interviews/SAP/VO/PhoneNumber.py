MAPPING = {
    '2' : ('a', 'b', 'c'),
    '3' : ('d', 'e', 'f'),
    '4' : ('g', 'h', 'i'),
    '5' : ('j', 'k', 'l'),
    '6' : ('m', 'n', 'o'),
    '7' : ('p', 'q', 'r', 's'),
    '8' : ('t', 'u', 'v'),
    '9' : ('w', 'x', 'y', 'z')
}

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        results = [] 
        
        if not digits:
            
            return results 
        
        string = "" 
        index = 0 
        
        self.dfs(digits, index, string, results)

        return results 
    
    def dfs(self, digits, index, string, results):
        
        if index == len(digits):
            results.append(string)
            return 
        
        for c in MAPPING[digits[index]]:
            
            self.dfs(digits, index + 1, string + c, results)
            
        return results 