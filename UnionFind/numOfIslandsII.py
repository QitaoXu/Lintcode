from collections import deque 

DIRECTIONS = [
    [0, 1], [0, -1], [1, 0], [-1, 0]
    ]
"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param n: An integer
    @param m: An integer
    @param operators: an array of point
    @return: an integer array
    """
    def numIslands2(self, n, m, operators):
        # write your code here
        
        results = [] 
        island = set()
        self.count = 0 
        self.father = {}
        
        for operator in operators:
            
            x, y = operator.x, operator.y
            
            if (x, y) in island:
                
                results.append(self.count)
                
                continue 
            
            island.add((x, y))
            
            self.father[(x, y)] = (x, y)
            
            self.count += 1 
            
            for dx, dy in DIRECTIONS:
                
                nx, ny = x + dx, y + dy 
                
                if (nx, ny) in island:
                    self.union((x, y), (nx, ny))
                    
            results.append(self.count)
            
        return results
        
    def union(self, a, b):
        
        root_a = self.find(a)
        root_b = self.find(b)
        
        if root_a == root_b:
            
            return 
            
        self.father[root_b] = root_a
        
        self.count -= 1 
        
    def find(self, point):
        
        path = [] 
        
        while self.father[point] != point:
            
            path.append(point)
            
            point = self.father[point]
            
        for p in path:
            
            self.father[p] = point 
            
        return point 

        
                
                
                
                
                
                
                
                
                
                
                
                
                
                