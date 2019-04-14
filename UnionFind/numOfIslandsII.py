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

class UnionFind:
    
    def __init__(self):
        
        self.father = {}
        self.count = 0 
        
    def union(self, a, b):
        
        root_a = self.find(a)
        root_b = self.find(b)
        
        if root_a == root_b:
            
            return 
        
        self.father[root_b] = root_a
        self.count -= 1 
        
    def find(self, point):
        
        path = [] 
        
        while point != self.father[point]:
            
            path.append(point)
            
            point = self.father[point]
            
        for p in path:
            
            self.father[p] = point 
            
        return point 
        
        
        
class Solution:
    """
    @param n: An integer
    @param m: An integer
    @param operators: an array of point
    @return: an integer array
    """
    def numIslands2(self, n, m, operators):
        # write your code here
        
        islands = set()
        
        results = []
        
        uf = UnionFind()
        
        for operator in operators:
            
            x, y = operator.x, operator.y
            
            if (x, y) in islands:
                
                results.append(uf.count)
                
                continue 
            
            islands.add((x, y))
            
            uf.father[(x, y)] = (x, y)
            uf.count += 1 
            
            for dx, dy in DIRECTIONS:
                
                nx, ny = x + dx, y + dy 
                
                if (nx, ny) in islands:
                    
                    uf.union((x, y), (nx, ny))
                    
            results.append(uf.count)
            
        return results
                