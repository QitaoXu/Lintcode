from collections import deque
class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """
    def sequenceReconstruction(self, org, seqs):
        # write your code here
        graph = self.build_graph(seqs)
        order = self.topo_sort(graph)
        
        if order == org:
            return True 
            
        return False 
        
    def build_graph(self, seqs):
        
        graph = {} 
        
        for seq in  seqs:
            for node in seq:
                if node not in graph:
                    graph[node] = set() 
                    
        for seq in seqs:
            for i in range(1, len(seq)):
                graph[seq[i - 1]].add(seq[i])
                
        return graph 
        
    def get_indegrees(self, graph):
        
        indegrees = { node : 0 for node in graph }
        
        for node in graph:
            for neighbor in graph[node]:
                indegrees[neighbor] += 1 
                
        return indegrees 
        
    def topo_sort(self, graph):
        
        indegrees = self.get_indegrees(graph)
        
        queue = deque() 
        
        for node in indegrees:
            if indegrees[node] == 0:
                queue.append(node)
                
        order = [] 
        
        while queue:
            
            if len(queue) > 1:
                return None 
                
            node = queue.popleft() 
            
            order.append(node)
            
            for neighbor in graph[node]:
                indegrees[neighbor] -= 1 
                
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
                    
        if len(order) == len(graph):
            return order 
            
        return None 
        
        
        
        
        
        
        