class ConnectingGraph2:
    """
    @param: n: An integer
    """
    def __init__(self, n):
        # do intialization if necessary
        self.father = { i : i for i in range(1, n + 1)}
        self.count = n 
        self.root_to_count = { i : 1 for i in range(1, n + 1) } 

    """
    @param: a: An integer
    @param: b: An integer
    @return: nothing
    """
    def connect(self, a, b):
        # write your code here
        
        if a not in self.father or b not in self.father:
            
            return 
        
        self.union(a, b)

    """
    @param: a: An integer
    @return: An integer
    """
    def query(self, a):
        # write your code here
        
        if a not in self.father:
            
            return 0 
            
        root_a = self.find(a)
        
        return self.root_to_count[root_a]
        
    def union(self, a, b):
        
        root_a = self.find(a)
        root_b = self.find(b)
        
        if root_a == root_b:
            
            return 
        
        self.father[root_b] = root_a
        
        self.root_to_count[root_a] += self.root_to_count[root_b]
        
        del self.root_to_count[root_b]
        
        self.count -= 1 
        
    def find(self, point):
        
        path = [] 
        
        while point != self.father[point]:
            
            path.append(point)
            
            point = self.father[point]
            
        for p in path:
            
            self.father[p] = point 
            
        return point 