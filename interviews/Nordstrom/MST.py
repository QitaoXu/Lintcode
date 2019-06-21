class UnionFind:

    def __init__(self):

        self.father = {} 
        self.count = 0 

    def union(self, a, b):

        root_a = self.find(a)
        root_b = self.find(b) 

        if root_a == root_b:
            return False 

        self.father[root_b] = root_a 
        self.count -= 1 
        return True 

    def find(self, point):

        path = [] 

        while point != self.father[point]:

            path.append(point)

            point = self.father[point]

        for p in path:

            self.father[p] = point 

        return point 

class Connection:

    def __init__(self, start, end, weight):

        self.start = start 
        self.end = end 
        self.weight = weight 

    def __lt__(self, other):

        if self.weight == other.weight:

            if self.start == other.start:
                return self.end < other.end 

            return self.start < other.start 

        return self.weight < other.weight 


class Solution:

    def generateMST(self, sources, destinations, weights):

        connections = [] 

        for i in range(len(sources)):

            connection = Connection(sources[i], destinations[i], weights[i]) 
            connections.append(connection)

        connections = sorted(connections) 

        uf = UnionFind()

        for connection in connections:

            for node in (connection.start, connection.end):

                if node not in uf.father:
                    uf.father[node] = node 
                    uf.count += 1 

        path = [] 

        for connection in connections:

            if uf.union(connection.start, connection.end):

                path.append(connection) 

        return path 

        