from collections import deque

class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        # write your code here
        
        graph = self.build_graph(numCourses, prerequisites)
        return self.topo_sort(graph)
        
        
    def build_graph(self, numCourses, prerequisites):
        
        graph = {}
        for node in range(numCourses):
            
            graph[node] = set() 
            
        for (post, pre) in prerequisites:
            graph[pre].add(post)
            
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
        
        
        for node in graph:
            if indegrees[node] == 0:
                queue.append(node)
                
        order = [] 
        
        while queue:
            
            node = queue.popleft() 
            
            order.append(node)
            
            for neighbor in graph[node]:
                indegrees[neighbor] -= 1 
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
                    
        if len(order) == len(graph):
            return order 
            
        return []