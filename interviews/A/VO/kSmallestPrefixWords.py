from heapq import heappush, heappop 

class Point:

    def __init__(self, word):
        self.word = word
        self.length = len(word)

    def __lt__(self, other):
        if self.length == other.length:
            return self.word < other.word
        return self.length > other.length

    
class Solution:

    def findKSmallestWordsWithPrefix(self, prefix, k, words):

        heap = []
        res = [] 
        counter = 1 

        for word in words:

            if word.startswith(prefix):

                heappush(heap, (-len(word), word))

                counter += 1 

                if len(heap) > k:
                    heappop(heap)

        while heap:

            _,  word = heappop(heap)

            res.append(word)

        return res 

class Solution2:

    def findKSmallestWordsWithPrefix(self, prefix, k, words):

        heap = []
        res = [] 
        counter = 1 

        for word in words:

            if word.startswith(prefix):

                heappush(heap, Point(word))

                counter += 1 

                if len(heap) > k:
                    heappop(heap)

        while heap:

            point = heappop(heap)

            res.append(point.word)

        return res 


solution = Solution()
solution2 = Solution2()

prefix="se"
words = ["set", "settle", "seattle", "size", "sea"]

print(solution.findKSmallestWordsWithPrefix(prefix, 2, words))
print(solution2.findKSmallestWordsWithPrefix(prefix, 2, words))

        