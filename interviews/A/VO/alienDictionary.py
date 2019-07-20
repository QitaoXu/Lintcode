from collections import deque 
from heapq import heappush, heappop, heapify

class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alienOrder(self, words):
        # Write your code here
        
        graph = self.build_graph(words)
        
        order = self.topo_sort(graph)
        
        return ''.join(order)
    
    def build_graph(self, words):
        
        graph = {}
        
        for word in words:
            for alpha in word:
                if alpha not in graph:
                    graph[alpha] = set()
        
        n = len(words)
        
        for i in range(n - 1):
            for j in range( min( len(words[i]), len(words[i + 1]) ) ):
                if words[i][j] != words[i + 1][j]:
                    graph[words[i][j]].add(words[i + 1][j])
                    break
                
        return graph 
                   
        
                
    def get_indegrees(self, graph):
        
        indegrees = { node : 0 for node in graph }
        
        for node in graph:
            for neighbor in graph[node]:
                
                indegrees[neighbor] += 1 
                
        return indegrees 
        
        
    def topo_sort(self, graph):
        
        
        indegrees = self.get_indegrees(graph)
        
        queue = [] 
        
        for node in graph:
            if indegrees[node] == 0:
                queue.append(node)
                
        heapify(queue)
        
        order = [] 
        
        while queue:
            
            node = heappop(queue)
            
            order.append(node)
            
            for neighbor in graph[node]:
                
                indegrees[neighbor] -= 1
                
                if indegrees[neighbor] == 0:
                    heappush(queue, neighbor)
                    
        if len(order) == len(graph):
            return order 
            
        return []
            

solution = Solution()
words = ["ze","yf","xd","wd","vd","ua","tt","sz","rd", "qd","pz","op","nw","mt","ln","ko","jm","il", "ho","gk","fa","ed","dg","ct","bb","ba"]

print(solution.alienOrder(words))
                
                
                
            