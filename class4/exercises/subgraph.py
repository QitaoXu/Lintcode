from collections import deque

"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param {UndirectedGraphNode[]} nodes a array of undirected graph node
    @return {int[][]} a connected set of a undirected graph
    """
    def connectedSet(self, nodes):
        # write your code here
        
        
        visited = set() 
        results = []
        
        
        for node in nodes:
            
            if node in visited:
                continue 
            
            queue = deque()
            queue.append(node)
            subgraph = []
            visited.add(node)
            
            while queue:

                head = queue.popleft()
                subgraph.append(head.label)
                
                for neighbor in head.neighbors:
                    
                    if neighbor in visited:
                        continue 
                    
                    queue.append(neighbor)
                    visited.add(neighbor)
                    
            subgraph.sort()
            results.append(subgraph)
            
        return results 
                
                
                
                
                
                
                
                
                
                
                
                
                
                
            
            