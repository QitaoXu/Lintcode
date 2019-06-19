from collections import deque 

class Solution:

    def cutLeastTrees(self, trees):

        queue = deque() 
        distance = {} 

        queue.append(tuple(trees)) 
        distance[tuple(trees)] = 0 

        while queue: 

            size = len(queue) 

            for _ in range(size):

                node = queue.popleft() 

                if self.is_valid(node):
                    return distance[node], node  

                for neighbor in self.get_neighbors(node):

                    if neighbor in distance:
                        continue 

                    queue.append(neighbor)
                    distance[neighbor] = distance[node] + 1 

        return -1 


    def get_neighbors(self, trees):

        neighbors = [] 

        trees = list(trees) 

        for i in range(len(trees)): 

            left = trees[:i]
            right = trees[i + 1:]

            neighbor = left + right 
            neighbors.append(tuple(neighbor))

        return neighbors

    def is_valid(self, trees):

        return self.is_asending(trees) or self.is_descending(trees) or self.is_asending_descending(trees) 

    def is_asending(self, trees):

        if len(trees) <= 1:
            return False 

        for i in range(1, len(trees)):

            if trees[i] <= trees[i - 1]:
                return False 

        return True 

    def is_descending(self, trees):

        if len(trees) <= 1:
            return False  

        for i in range(1, len(trees)):

            if trees[i] >= trees[i - 1]:
                return False 

        return True 

    def is_asending_descending(self, trees):

        if len(trees) <= 1:
            return True 

        for i in range(len(trees)):

            left = trees[:i] 
            right = trees[i:] 

            if self.is_asending(left) and self.is_descending(right):
                return True 

        return False 

solution = Solution() 

trees = [3, 17, 4, 12, 5, 6, 2, 1]
# trees = [9, 8, 7, 12, 3, 99]
# trees = [9, 9, 9, 9, 9]

print(solution.cutLeastTrees(trees)) 
