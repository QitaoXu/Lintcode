class Solution:

    def beforeAndAfter(self, phrases):

        first_word_to_index = {} 
        last_word_to_index = {} 

        result = [] 

        for i in range(len(phrases)):

            words = phrases[i].split()

            if words[0] not in first_word_to_index:
                first_word_to_index[words[0]] = [] 

            first_word_to_index[words[0]].append(i)

            if words[-1] not in last_word_to_index:
                last_word_to_index[words[-1]] = [] 

            last_word_to_index[words[-1]].append(i)

        for last_word in last_word_to_index.keys():

            if last_word in first_word_to_index:
                
                for before_index in last_word_to_index[last_word]:
                    before = phrases[before_index]

                    for after_index in first_word_to_index[last_word]:
                        after = phrases[after_index]
                        index = after.find(' ')
                        after = after[index : ]

                        result.append(before + after) 
            
        return result 

solution = Solution()

phrases = [
    'mission statement',
    'a quick bite to eat',
    'a chip off the old block',
    'chocolate bar',
    'mission impossible',
    'a man on a mission',
    'block party',
    'eat my words',
    'bar of soap'
]

# print(solution.beforeAndAfter(phrases))

for state in solution.beforeAndAfter(phrases):
    print(state)