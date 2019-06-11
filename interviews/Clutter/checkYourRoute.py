from heapq import heappush, heappop

class Solution:

    def checkYourRoute(self, nodes, sources, destinantions, weights, end):

        graph = self.build_graph(nodes, sources, destinantions)
        edge_to_weight = self.get_edge_to_weight(sources, destinantions, weights)

        shortest_dis = self.dijkstra(graph, edge_to_weight)

        # print(shortest_dis)

        results = [] 

        self.dfs(graph, edge_to_weight, shortest_dis, 0, 1, end, [1], results)

        for path in results:
            print(path) 

        return self.formatOutput(results, sources, destinantions)

    def dfs(self, graph, edge_to_weight, shortest_dis, cur_cost, cur, end, path, results):

        if cur == end:

            if cur_cost == shortest_dis[end]:
                results.append(path[:])
            
            return  

        for neighbor in graph[cur]:

            if cur_cost + edge_to_weight[(cur, neighbor)] > shortest_dis[end]:
                continue 

            path.append(neighbor)

            next_cost = cur_cost + edge_to_weight[(cur, neighbor)]

            self.dfs(graph, edge_to_weight, shortest_dis, next_cost, neighbor, end, path, results)

            path.pop()

    def formatOutput(self, results, sources, destinantions):

        edges_to_index = self.get_edge_to_index(sources, destinantions)

        output = ["NO" for _ in range(len(sources))] 

        for path in results:

            for start in range(0, len(path) - 1):
                end = start + 1 

                index = edges_to_index[(path[start], path[end])] 
                output[index] = "YES"

        return output

    def get_edge_to_index(self, sources, destinantions):

        edges_to_index = {} 

        for i in range(len(sources)):

            edges_to_index[(sources[i], destinantions[i])] = i 
            edges_to_index[(destinantions[i], sources[i])] = i 

        return edges_to_index 

    def build_graph(self, nodes, sources, destinantions):

        graph = {node : set() for node in range(1, nodes + 1)}  

        for i in range(len(sources)):

            graph[sources[i]].add(destinantions[i])
            graph[destinantions[i]].add(sources[i])

        return graph 

    def get_edge_to_weight(self, sources, destinantions, weights):

        edge_to_weight = {} 

        for i in range(len(sources)):

            edge_to_weight[(sources[i], destinantions[i])] = weights[i]
            edge_to_weight[(destinantions[i], sources[i])] = weights[i]

        return edge_to_weight

    def dijkstra(self, graph, edge_to_weight):

        d = {i : max(edge_to_weight.values()) + 1 for i in range(1, len(graph) + 1)}
        # prev = {i : None for i in range(1, len(graph) + 1)}

        d[1] = 0 
        S = set()

        Q = [] 
        for node in graph:
            heappush(Q, (d[node], node))

        while Q:

            _, u = heappop(Q)

            S.add(u)

            for v in graph[u]:
                edge = (u, v) 

                if d[v] > d[u] + edge_to_weight[edge]:
                    d[v] = d[u] + edge_to_weight[edge]

        return d 



solution = Solution()

nodes = 5 
sources = [1, 2, 3, 4, 5, 1, 5]
destinantions = [2, 3, 4, 5, 1, 3, 3]
weights = [1, 1, 1, 1, 3, 2, 1]
end = 5 

output = solution.checkYourRoute(nodes, sources, destinantions, weights, end)

print(output)
    

        