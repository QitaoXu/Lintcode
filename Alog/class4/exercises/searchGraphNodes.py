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
    @param: graph: a list of Undirected graph node
    @param: values: a hash mapping, <UndirectedGraphNode, (int)value>
    @param: node: an Undirected graph node
    @param: target: An integer
    @return: a node
    """
    def searchNode(self, graph, values, node, target):
        # write your code here
        
        queue = deque()
        seen = set() 
        
        queue.append(node)
        seen.add(node)
        
        while queue:
            
            size = len(queue)
            
            for _ in range(size):
                
                head = queue.popleft() 
                
                if head in values:
                    if values[head] == target:
                        return head
                
                for neighbor in head.neighbors:
                    
                    if neighbor in seen:
                        continue 
                        
                    else:
                        seen.add(neighbor)
                        queue.append(neighbor)
                        
        return None 
                
                
                
                
                
                
                
                
        