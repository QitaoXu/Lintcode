import fileinput

# for line in fileinput.input():
#     print(line.rstrip())

class UnionFind:

    def __init__(self, n, father):
        self.count = n 
        self.father = father 

    def union(self, a, b):

        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return 

        self.father[root_b] = root_a 

        self.count -= 1 

    def find(self, point):

        path = []

        while self.father[point] != -1:

            path.append(point)
            point = self.father[point]

        for p in path:
            self.father[p] = point 

        return point 

class Solution:

    def groupAnimals(self, n, spieces):

        


        return n 





file = open("testfile.txt", "r")

i = 0 

n = 0
spieces = [] 

for line in file:

    print(line.rstrip().split())

    this_line = line.rstrip().split()

    if len(this_line) == 1:
        n = int(this_line[0])
        spieces = [-1 for _ in range(n)]

    else:
        spieces[int(this_line[0])] = int(this_line[1])

    i += 1 

for j in range(n):
    print(str(j) + " <- " + str(spieces[j]))