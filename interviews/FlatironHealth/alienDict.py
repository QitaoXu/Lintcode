from heapq import heappush, heappop, heapify 
class Solution:
    def alienOrder(self, words):
        
        graph = self.build_graph(words)
        
        order = self.topo_order(graph)
        
        return "".join(order)
    
    def build_graph(self, words):
        
        graph = {} 
        
        for word in words:
            for c in word:
                
                if c not in graph:
                    graph[c] = set()
                    
        n = len(words)
        
        for i in range(0, n - 1):
            
            for j in range(0, min(len(words[i]), len(words[i + 1]) ) ):
                
                if words[i][j] != words[i + 1][j]:
                    
                    graph[words[i][j]].add(words[i + 1][j])
                    
                    break 
                    
        return graph 
    
    def get_indegrees(self, graph):
        
        indegrees = {n : 0 for n in graph}
        
        for node in graph:
            for neighbor in graph[node]:
                indegrees[neighbor] += 1 
                
        return indegrees 
    
    def topo_order(self, graph):
        
        indegrees = self.get_indegrees(graph)
        
        queue = [] 
        
        for node in graph:
            
            if indegrees[node] == 0:
                queue.append(node)
                
        heapify(queue)
        order = []
        
        while queue:
            
            size = len(queue)
            
            for _ in range(size):
                
                node = heappop(queue)
                
                order.append(node)
                
                for neighbor in graph[node]:
                    
                    indegrees[neighbor] -= 1 
                    if indegrees[neighbor] == 0:
                        heappush(queue, neighbor)
                        
        if len(order) == len(graph):
            return order 
        
        return [] 
                        
                        
        