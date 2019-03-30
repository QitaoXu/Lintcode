class Solution:
    """
    @param str: A string
    @return: all permutations
    """
    def stringPermutation2(self, string):
        # write your code here
        
        results = [] 
        
        if string is None:
            return  results
            
        string = sorted(string)
        
        permutation = ""
        visited = [False for _ in string]
        
        self.dfs(string, permutation, visited, results)
        
        return results
    
    def dfs(self, string, permutation, visited, results):
        
        if len(permutation) == len(string):
            
            results.append(permutation[:])
            
            return 
        
        for i in range(0, len(string)):
            
            if visited[i] == True:
                continue 
            
            if i > 0 and string[i] == string[i - 1] and visited[i - 1] == False:
                continue 
            
            
            visited[i] = True 
            
            self.dfs(string, permutation + string[i], visited, results)
            
            visited[i] = False 