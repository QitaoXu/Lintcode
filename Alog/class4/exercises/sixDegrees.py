from collections import deque

"""
Definition for Undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: graph: a list of Undirected graph node
    @param: s: Undirected graph node
    @param: t: Undirected graph nodes
    @return: an integer
    """
    def sixDegrees(self, graph, s, t):
        # write your code here
        
        queue = deque()
        
        distance = {s : 0}
        
        queue.append(s)
        
        while queue:
            
            size = len(queue)
            
            for _ in range(size):
                
                node = queue.popleft()
                
                if node == t:
                    return distance[node]
                
                for neighbor in node.neighbors:
                    
                    if neighbor in distance:
                        continue 
                    
                    queue.append(neighbor)
                    distance[neighbor] = distance[node] + 1 
        return -1