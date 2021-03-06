from collections import deque
class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """
    def findLadders(self, start, end, dict):
        # write your code here
        
        results = [] 
        
        dict.add(start)
        dict.add(end)
        
        distance = {}
        
        self.bfs(end, start, distance, dict)
        
        self.dfs(start, end, [start], distance, dict, results)
        
        return results
    
    
    def bfs(self, start, end, distance, dictionary):
        
        queue = deque()
        queue.append(start)
        distance[start] = 0 
        
        while queue:
            
            size = len(queue)
            
            for _ in range(size):
                
                word = queue.popleft()
                
                for next_word in self.get_next_words(word):
                    
                    if next_word not in dictionary:
                        continue
                    
                    if next_word in distance:
                        continue 
                    
                    queue.append(next_word)
                    distance[next_word] = distance[word] + 1 
    
    def get_next_words(self, word):
        
        
        next_words = [] 
        
        
        for i in range(len(word)):
            
            left, right = word[:i], word[i + 1:]
            
            for c in "abcdefghijklmnopqrstuvwxyz":
                
                if c == word[i]:
                    continue 
                
                next_word = left + c + right 
                next_words.append(next_word)
                
        return next_words
        
    def dfs(self, curt, target, path, distance, dictinoary, results):
        
        if curt == target:
            results.append(path.copy())
            return 
        
        
        for next_word in self.get_next_words(curt):
            
            if next_word not in dictinoary:
                continue
            
            if distance[next_word] != distance[curt] - 1:
                continue
            
            path.append(next_word)
            
            self.dfs(next_word, target, path, distance, dictinoary, results)
            
            path.pop()
            