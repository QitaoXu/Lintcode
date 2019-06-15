from collections import deque 

class UnionFind:
    
    def __init__(self, n):
        
        self.father = { i : i for i in range(n)}
        self.count = n 
        
    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        
        if root_a != root_b:
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
    def findCircleNum(self, M) -> int:
        
        if not M or not M[0]:
            return 0 
        
        n = len(M)
        
        uf = UnionFind(n)
        
        for i in range(n):
            for j in range(n):
                
                if M[i][j] == 1:
                    uf.union(i, j)
                    
        return uf.count 