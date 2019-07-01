class UnionFind:

    def __init__(self, n):

        self.count = n 
        self.father = {i : i for i in range(n)} 
        self.father_to_points = {i : [i] for i in range(n)} 

    def union(self, a, b):

        root_a = self.find(a) 
        root_b = self.find(b) 

        if root_a == root_b:
            return 

        self.father[root_b] = self.father[root_a] 
        self.father_to_points[root_a] += self.father_to_points[root_b] 
        self.count -= 1 

    def find(self, point):

        path = [] 

        while self.father[point] != point: 

            path.append(point) 
            point = self.father[point] 

        for p in path:

            self.father[p] = point 

        return point 

class Point:

    def __init__(self, weight, neighbor):
        self.weight = weight 
        self.neighbor = neighbor 

    @staticmethod
    def build_graph(self, graph_table, weights):

        graph = [] 

        for node in graph_table:

            for neighbor in graph_table[node]:

                point = Point(weights[(node, neighbor)], neighbor) 

                graph.append(point) 

        return graph 

class Solution:

    def findMinCircle(self, graph):

        uf = UnionFind(len(graph)) 

        for node in graph:

            neighbor = node.next 

            uf.union(node, neighbor) 

        max_circle_count = -1 

        for father in uf.father_to_points.keys():
            circle_count = self.compute_circle(uf.father_to_points[father], graph) 

            if circle_count > max_circle_count:
                max_circle_count = circle_count 

        return max_circle_count

    def compute_circle(self, points, graph):

        count = 0 

        for point in points:
            
            count += point.weight 

        return count 



