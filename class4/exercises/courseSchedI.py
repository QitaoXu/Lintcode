from collections import deque
class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def canFinish(self, numCourses, prerequisites):
        # write your code here
        
    #     indegrees = {x : 0 for x in range(numCourses)}
    #     pre_post = {x : [] for x in range(numCourses)}
        
    #     for post, pre in prerequisites:
    #         indegrees[post] += 1 
    #         pre_post[pre].append(post)
        
    #     start_courses = [ x for x in indegrees.keys() if indegrees[x] == 0]
    #     queue = deque(start_courses) 
        
    #     # count = 0 
    #     order = []
        
    #     while queue:
            
    #         course = queue.popleft()
    #         # count += 1
    #         order.append(course)
            
    #         for post in pre_post[course]:
    #             indegrees[post] -= 1 
    #             if indegrees[post] == 0:
    #                 queue.append(post)
                    
    #     return len(order) == numCourses
        
        graph = self.build_graph(numCourses, prerequisites)
        return self.topo_sort(graph)
        
        
    def build_graph(self, numCourses, prerequisites):
        
        graph = {} 
        
        for node in range(numCourses):
            if node not in graph:
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
            return True 
            
        return False 