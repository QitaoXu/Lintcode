from heapq import heappop, heappush

class Item:
    
    def __init__(self, count, word):
        
        self.count = count
        self.word = word
        
    def __lt__(self, other):
        
        if self.count == other.count:
            return self.word > other.word 
            
        return self.count < other.count 
        
    def __gt__(self, other):
        
        if self.count == other.count:
            
            return self.word < other.word
            
        return self.count > other.count 
        
    def __eq__(self, other):
        
        return self.count == other.counnt and self.word == other.word 
        
        
class Solution:
    """
    @param words: an array of string
    @param k: An integer
    @return: an array of string
    """
    def topKFrequentWords(self, words, k):
        # write your code here
        
        count = {} 
        
        for word in words:
            
            count[word] = count.get(word, 0) + 1 
                
                
        heap = []
        
        for word in count:
            
            item = Item(count[word], word)
            
            heappush(heap, item)
            
            if len(heap) > k:
                
                heappop(heap)
                
        results = [] 
        
        while heap:
            
            item = heappop(heap)
            
            results.append(item.word)
            
        return results[::-1]