from collections import deque
"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    """
    @param: node: A undirected graph node
    @return: A undirected graph node
    """
    def cloneGraph(self, node):
        # write your code here
        start = node 
        
        if node is None:
            return node 
            
        nodes = self.getNodes(node)
        
        mapping = {}
        for node in nodes:
            mapping[node] = UndirectedGraphNode(node.label)
            
        for node in nodes:
            new_node = mapping[node]
            
            for neighbor in node.neighbors:
                new_neighbor = mapping[neighbor]
                new_node.neighbors.append(new_neighbor)
                
        return mapping[start]
        
    def getNodes(self, node):
        
        
        queue = deque()
        seen = set() 
        # results = set()
        
        queue.append(node)
        seen.add(node)
        # results.add(node)
        
        while queue:
            
            size = len(queue)
            
            for _ in range(size):
                
                cur_node = queue.popleft() 
                
                for neighbor in cur_node.neighbors:
                    
                    if neighbor in seen:
                        continue 
                    
                    queue.append(neighbor)
                    seen.add(neighbor)
                    # results.add(neighbor)
                    
        # return results
        return seen
        
        
                    
                    
        
        