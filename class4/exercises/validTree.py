from collections import deque 

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        # write your code here
        
        if len(edges) != n - 1:
            return False 
            
        neighbors = {node : set() for node in range(n) } 
        
        for pre, post in edges:
            neighbors[pre].add(post)
            neighbors[post].add(pre)
            
        queue = deque()
        visited = {} 
        
        queue.append(0)
        visited[0] = True 
        
        while queue:
            
            node = queue.popleft() 
            
            for neighbor in  neighbors[node]:
                
                if neighbor in visited:
                    continue 
                
                visited[neighbor] = True 
                queue.append(neighbor)
                
        if len(visited) == n:
            return True 
            
        return False 
                