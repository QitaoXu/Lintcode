class Solution:

    def isSubsetofCapacity(self, capacity, weights):

        weights.sort() 

        combination = []
        running_sum = 0
        index = 0

        return self.dfs(capacity, weights, index, combination, running_sum)

    def dfs(self, capacity, weights, index, combination, running_sum):

        if running_sum % capacity == 0 and running_sum != 0:
            print(combination)
            return True 

        if index == len(weights):
            return False 

        for weight in [0, weights[index]]:

            combination.append(weight)

            if self.dfs(capacity, weights, index + 1, combination, running_sum + weight):
                return True

            combination.pop()

        return False 

        
solution = Solution() 
capacity = 6
weights = [1, 3, 5, 11] 

print(solution.isSubsetofCapacity(capacity, weights))