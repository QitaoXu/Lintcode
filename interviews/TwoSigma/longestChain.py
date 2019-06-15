class Solution:

    def findLongestChain(self, words):

        words_set = set(words)

        words = sorted(words, key = lambda word : len(word)) 

        word_to_longest = {word : 1 for word in words} 

        longest = 0 

        for word in words:

            for neighbor in self.get_neighbors(word, words_set):

                if word_to_longest[neighbor] + 1 > word_to_longest[word]:
                    word_to_longest[word] = word_to_longest[neighbor] + 1 

            if word_to_longest[word] > longest:
                longest = word_to_longest[word] 

        return longest 

    def get_neighbors(self, word, words_set):
        neighbors = [] 

        for i in range(len(word)):

            left, right = word[:i], word[i + 1:] 

            if (left + right) in words_set:
                neighbors.append(left + right)

        return neighbors 

words = ["a", "b", "ba", "bca", "bda", "bdca"]

solution = Solution()

print(solution.findLongestChain(words))