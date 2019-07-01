class Solution:

    def getValidPairCount(self, pairs):

        if not pairs:
            return 0 

        count = 0
        pair_set = set() 

        for (x, y) in pairs:

            if (x, y) in pair_set:
                count += 1 

            else:
                pair_set.add((x, y)) 
                pair_set.add((y, x)) 

        return count 