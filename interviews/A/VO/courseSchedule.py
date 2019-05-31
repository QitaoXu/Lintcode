from collections import deque
class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def canFinish(self, numCourses, prerequisites):
        # write your code here
        
        graph = self.build_graph(numCourses, prerequisites)
        
        return self.topo_sort(graph)
        
    def build_graph(self, numCourses, prerequisites):
        
        graph = {}
        
        for node in range(numCourses):
            
            if node not in graph:
            
                graph[node] = set()
            
        for post, pre in prerequisites:
            
            graph[pre].add(post)
            
        return graph
        
    def get_in_degrees(self, graph):
        
        in_degress = { node : 0 for node in graph}
        
        for node in graph:
            
            for neighbor in graph[node]:
                
                in_degress[neighbor] += 1 
                
        return in_degress
        
    def topo_sort(self, graph):
        
        in_degress = self.get_in_degrees(graph)
        
        queue = deque()
        
        for node in graph:
            
            if in_degress[node] == 0:
                
                queue.append(node)
                
             
        order = [] 
        
        while queue:
            
            node = queue.popleft()
            
            order.append(node)
            
            for neighbor in graph[node]:
                
                in_degress[neighbor] -= 1 
                
                if in_degress[neighbor] == 0:
                    
                    queue.append(neighbor)
                    
        if len(order) == len(graph):
            
            return True 
            
        return False 
            
        