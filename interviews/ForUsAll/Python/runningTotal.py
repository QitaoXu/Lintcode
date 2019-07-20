class Solution:

    def canFirstWin(self, m, target):

        running_total = 0 

        num_set = set([i for i in range(1, m + 1)])

        for i in range(1, m + 1):

            running_total += max(num_set)
            num_set.remove(max(num_set)) 
            
            if running_total >= target:
                return True if i % 2 == 1 else False 

        return False 

            