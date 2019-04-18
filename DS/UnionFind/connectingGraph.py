class ConnectingGraph:
    """
    @param: n: An integer
    """
    def __init__(self, n):
        # do intialization if necessary
        self.father = { i : i for i in range(1, n + 1)}
        self.count = n 
    """
    @param: a: An integer
    @param: b: An integer
    @return: nothing
    """
    def connect(self, a, b):
        # write your code here
        
        if a not in self.father or b  not in self.father:
            
            return 
        
        self.union(a, b)

    """
    @param: a: An integer
    @param: b: An integer
    @return: A boolean
    """
    def query(self, a, b):
        # write your code here
        
        if a not in self.father or b not in self.father:
            
            return False 
        
        root_a = self.find(a)
        root_b = self.find(b)
        
        return root_a == root_b
        
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