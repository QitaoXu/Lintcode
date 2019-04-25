class Solution:

    def findTarget(self, dices, sides, target):
      
        print("\nnum of dices = %d, num of sides = %d, target = %d" %(dices, sides, target))

        results = []

        combination = [] 
        
        found = set()

        self.dfs(dices, 0, sides, combination, target, results, found)

        return results 

    def dfs(self, dices, start_index, sides, combination, target, results, found):

        if start_index == dices:
            if target == 0:
				#
                # filter duplicates and 
                # handle corner case like [4] is not a valid combination 
                # when dices = 2, sides = 4, target = 4 
                #
                if tuple(sorted(combination)) not in found and len(combination) == dices: 

                    results.append(combination.copy())
                    found.add(tuple(sorted(combination)))
                
            return 

        for i in range(start_index, dices):

            if target <= 0:

                return 

            for side in range(1, sides + 1):

                combination.append(side)
            
                self.dfs(dices, i + 1, sides, combination, target - side, results, found)

                combination.pop()

solution = Solution() 

print(solution.findTarget(3, 5, 10))
print(solution.findTarget(2, 3, 4))
print(solution.findTarget(2, 4, 4))
print(solution.findTarget(3, 4, 4))