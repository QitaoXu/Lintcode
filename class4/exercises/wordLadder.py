import collections
class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        # write your code here
        dict.add(end)
        
        # queue = collections.deque([start])
        # seen = set([start])
        queue = collections.deque()
        seen = set()
        
        queue.append(start)
        seen.add(start)
        
        distance = 0 
        
        while queue:
            
            distance += 1 
            
            size = len(queue)
            
            for _ in range(size):
                
                current_word = queue.popleft()
                
                if current_word == end:
                    return distance 
                
                for next_word in self.get_next_words(current_word):
                    if next_word not in dict or next_word in seen:
                        continue 
                    
                    queue.append(next_word)
                    seen.add(next_word)
                    
        return 0 
        
        
    def get_next_words(self, word):
        
        next_words = []
        
        for i in range(len(word)):
            
            left = word[: i]
            right = word[i + 1:]
            
            for c in 'abcdefghijklmnopqrstuvwxyz':
                
                if word[i] == c:
                    continue
                next_word = left + c + right 
                next_words.append(next_word)
                
        return next_words