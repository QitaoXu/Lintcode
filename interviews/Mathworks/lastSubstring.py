from heapq import heappush, heappop

class Item:

    def __init__(self, string):

        self.string = string 

    def __lt__(self, other):
        return self.string > other.string


class Solution:

    def findLastSubstring(self, string):

        results = set()
        heap = [] 

        for start_index in range(0, len(string)):

            for end_index in range(start_index + 1, len(string) + 1):

                sub_string = string[start_index : end_index]

                if sub_string not in results:
                    results.add(sub_string)

                    heappush(heap, Item(sub_string))

        return heap[0].string 

solution = Solution()
string = "aaauuuuuoisjosmi"
print(solution.findLastSubstring(string))




       