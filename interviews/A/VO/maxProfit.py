class Solution:
    def __init__(self):
        self.maxProfit = 0

    def findMaxProfit(self, length, lengthToProfits, target):

        if not length or not lengthToProfits:
            return 0 

        self.dfs(length, lengthToProfits, [], target)

        return self.maxProfit 

    def dfs(self, length, lengthToProfits, combination, target):

        if target == 0:

            curt_profit = 0

            for l in combination:
                curt_profit += lengthToProfits[l]

            self.maxProfit = max(self.maxProfit, curt_profit)
            return 

        for l in length:

            if target - l < 0:
                break 

            combination.append(l)

            self.dfs(length, lengthToProfits, combination, target - l)

            combination.pop()

length = [1, 2, 3]
lengthToProfits = {1 : 4, 2 : 5, 3 : 6}
target = 3 

solution = Solution()

print(solution.findMaxProfit(length, lengthToProfits, target))


