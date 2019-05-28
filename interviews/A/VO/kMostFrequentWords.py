from collections import OrderedDict
class Solution:

    def findKMostFrequentWords(self, s):

        word_to_count = OrderedDict()
        word = ""

        s = s.lower() + " "

        for c in s:

            if c.isalpha():

                word += c  

            else:

                if len(word) > 0:

                    word_to_count[word] = word_to_count.get(word, 0) + 1 

                word = ""

        return word_to_count 

solution = Solution()

string = "Bob hit a ball, the hit BALL flew far after it was hit."

for word, count in solution.findKMostFrequentWords(string).items():

    print(word + " " + str(count))



