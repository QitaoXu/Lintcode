from heapq import heappush, heappop, _siftdown

import sys 

class Solution:

    def checkYourRoute(self, nodes, sources, destinations, weights, target):

        graph = self.buildGraph(nodes, sources, destinations) 
        edgeWeights = self.getEdgeWeights(sources, destinations, weights) 
        start = 1 
        shortestDistances = self.getShortestDistances(graph, start, edgeWeights) 

        paths = [] 
        path = [start] 
        cost = 0 

        if shortestDistances[target] != sys.maxsize:# target can be reached 

            self.getAllPaths(graph, edgeWeights, shortestDistances, start, cost, target, path, paths) 

        return self.normalizePaths(sources, destinantions, paths)

    def normalizePaths(self, sources, destinantions, paths):

        edgeIndex = self.getEdgeIndex(sources, destinantions) 

        results = ["NO" for _ in range(len(sources))] 

        for path in paths:

            for start in range(len(path) - 1):

                end = start + 1 
                edge = (path[start], path[end]) 

                index = edgeIndex[edge] 

                results[index] = "YES" 

        return results

    def getEdgeIndex(self, sources, destinantions):

        edgeIndex = {} 

        for index in range(len(sources)):

            edge_toward = (sources[index], destinantions[index]) 
            edge_back = (destinantions[index], sources[index]) 

            edgeIndex[edge_toward] = index 
            edgeIndex[edge_back] = index 

        return edgeIndex 

            

    def getAllPaths(self, graph, edgeWeights, shortestDistances, node, cost, target, path, paths):


        if node == target: 

            if cost == shortestDistances[target]:
                paths.append(path.copy()) 

            return 

        for neighbor in graph[node]:

            if cost + edgeWeights[(node, neighbor)] > shortestDistances[neighbor]:
                continue 

            path.append(neighbor) 

            new_cost = cost + edgeWeights[(node, neighbor)]

            self.getAllPaths(graph, edgeWeights, shortestDistances, neighbor, new_cost, target, path, paths) 

            path.pop()


    def buildGraph(self, nodes, sources, destinations):
        graph = {node : set() for node in range(1, nodes + 1)} 

        for index in range(len(sources)):

            graph[sources[index]].add(destinations[index]) 
            graph[destinations[index]].add(sources[index]) 

        return graph 

    def getEdgeWeights(self, sources, destinations, weights):

        edgeWeights = {} 

        for index in range(len(sources)):

            edge_toward = (sources[index], destinations[index]) 
            edge_back = (destinations[index], sources[index]) 

            edgeWeights[edge_toward] = weights[index] 
            edgeWeights[edge_back] = weights[index] 

        return edgeWeights 

    def getShortestDistances(self, graph, start, edgeWeights):

        d = {node : sys.maxsize for node in graph.keys()} 
        previous = {node : None for node in graph.keys()}

        d[start] = 0 
        seen = set([start]) 

        heap = [] 
        end_to_item = {} 

        for neighbor in graph[start]:
            edge = (start, neighbor) 
            d[neighbor] = edgeWeights[edge] 
            item = [edgeWeights[edge], start, neighbor] 
            heappush(heap, item) 
            end_to_item[neighbor] = item 

        
        while heap:

            _, prev, node = heappop(heap) 
            previous[node] = prev 

            if node not in seen:

                seen.add(node)

                for neighbor in graph[node]:

                    if neighbor in end_to_item:

                        edge = (node, neighbor) 

                        if d[neighbor] > d[node] + edgeWeights[edge]:
                            d[neighbor] = d[node] + edgeWeights[edge] 

                            end_to_item[neighbor][0] = d[neighbor] 
                            end_to_item[neighbor][1] = node 

                            _siftdown(heap, 0, heap.index(end_to_item[neighbor])) 

                        else:

                            d[neighbor] = d[node] + edgeWeights[edge] 

                            item = [d[neighbor], node, neighbor] 

                            heappush(heap, item) 

                            end_to_item[neighbor] = item 

        return d 





solution = Solution()

nodes = 5 
sources = [1, 2, 3, 4, 5, 1, 5]
destinantions = [2, 3, 4, 5, 1, 3, 3]
weights = [1, 1, 1, 1, 3, 2, 1]
end = 5 

output = solution.checkYourRoute(nodes, sources, destinantions, weights, end)

print(output)
    