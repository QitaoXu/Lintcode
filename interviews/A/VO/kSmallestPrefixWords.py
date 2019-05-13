from heapq import heappush, heappop 
class Solution:

    def findKSmallestWordsWithPrefix(self, prefix, k, words):

        heap = []
        res = [] 
        counter = 1 

        for word in words:

            if word.startswith(prefix):

                heappush(heap, (-len(word), -counter, word))

                counter += 1 

                if len(heap) > k:
                    heappop(heap)

        while heap:

            _, _, word = heappop(heap)

            res.append(word)

        return res 


solution = Solution()

prefix="sea"
words = ["set", "settle", "seattle", "size", "sea"]

print(solution.findKSmallestWordsWithPrefix(prefix, 2, words))

        