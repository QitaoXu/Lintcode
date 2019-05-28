TABLE = { chr(i + ord('a')) : chr((i + 3) % 26 + ord('a')) for i in range(26)}

class Solution:

    def findShortestStepsToGoBack(self, word):

        next_word = self.get_next_word(word)

        count = 1 

        while next_word != word:

            next_word = self.get_next_word(next_word)

            count += 1 

        return count 


    def get_next_word(self, word):

        next_word = [] 

        for i in range(len(word)):

            next_word.append(self.query(word[i]))

        return "".join(next_word)

    def query(self, character):

        return TABLE[character]


            

            
                        

                




