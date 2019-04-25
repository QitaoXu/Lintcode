from collections import deque 
class Solution:

    def findShortestStepToOne(self, n):

        print("num = %d" % (n))

        if n < 1:
            return -1

        queue = deque()
        queue.append(n) 
        distance = {n : 0} 

        while queue:

            size = len(queue)

            for _ in range(size):

                cur = queue.popleft()

                if cur == 1:

                    return distance[cur]

                for neighbor in self.get_neighbors(cur):

                    if neighbor in distance:
                        continue 

                    queue.append(neighbor)
                    distance[neighbor] = distance[cur] + 1 

        return -1 

    def get_neighbors(self, num):

        neighbors = [] 

        if num % 2 == 0 and num > 1:
            neighbors.append(num // 2)

        if num % 3 == 0 and num > 2:
            neighbors.append(num // 3)

        if num > 2:
            neighbors.append(num - 1)

        return neighbors

solution = Solution()
print(solution.findShortestStepToOne(7))



