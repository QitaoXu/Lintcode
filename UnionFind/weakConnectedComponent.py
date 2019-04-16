"""
Definition for a directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: nodes: a array of Directed graph node
    @return: a connected set of a directed graph
    """
    def connectedSet2(self, nodes):
        # write your code here
        
        self.father = { node.label : node.label for node in nodes }
        self.count = len(nodes)
        self.root_to_nodes = { node.label : set([node.label]) for node in nodes }
        
        for node in nodes:
            
            for neighbor in node.neighbors:
                
                self.union(node.label, neighbor.label)
            
            
        res = [] 
        
        for nodes_set in self.root_to_nodes.values():
            
            res.append(sorted(list(nodes_set)))
            
        return res 
        
    def union(self, a, b):
        
        root_a = self.find(a)
        root_b = self.find(b)
        
        if root_a == root_b:
            
            return 
        
        self.father[root_b] = root_a
        
        self.count -= 1 
        
        for node in self.root_to_nodes[root_b]:
            
            self.root_to_nodes[root_a].add(node)
            
        del self.root_to_nodes[root_b]
                
    def find(self, point):
        
        path = [] 
        
        while point != self.father[point]:
            
            path.append(point)
            
            point = self.father[point]
            
        for p in path:
            
            self.father[p] = point 
            
        return point 