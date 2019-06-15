from collections import deque 
# Problem: least operations to go to target song from current song
        # Modelize this problem as:
        # "in a simple graph, given source and destination, 
        # find the shortest distance from source to destination." 

# Solution: BFS(Breadth First Search) 
        # One of BFS's features is to solve shortest distance problem 
        # in simply graph with known source and destination 

class Solution:

    def playlist(self, songs, k, target):
        
        queue = deque()
        distance = {}

        queue.append(k)
        distance[k] = 0 

        while queue:

            size = len(queue)

            for _ in range(size):

                index = queue.popleft()

                if songs[index] == target:
                    return distance[index] 

                for neighbor in self.get_neighbors(index, songs):

                    if neighbor in distance:
                        continue 

                    queue.append(neighbor)
                    distance[neighbor] = distance[index] + 1 

        return -1 

    def get_neighbors(self, index, songs):

        n = len(songs) 

        neighbors = [] 
        neighbors.append((index + 1) % n)
        neighbors.append((index - 1) % n) 

        return neighbors 



solution = Solution()
songs = ["wheniseeyouagain",
         "borntorun",
         "cecelia",
         "lovethewayyoulie",
         "bornthisway"
         "nothingelsematters",
         "cecelia"]

k = 0
target = "cecelia"

print(solution.playlist(songs, k, target))
