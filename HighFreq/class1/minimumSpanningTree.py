'''
Definition for a Connection
class Connection:

    def __init__(self, city1, city2, cost):
        self.city1, self.city2, self.cost = city1, city2, cost
'''
class Solution:
    # @param {Connection[]} connections given a list of connections
    # include two cities and cost
    # @return {Connection[]} a list of connections from results
    def lowestCost(self, connections):
        # Write your code here
        if not connections:
            return []
        
        self.father = {} 
        self.count = 0 
        results = [] 
        
        connections.sort(key = lambda x:(x.cost, x.city1, x.city2))
        
        for connection in connections:
            
            for city in (connection.city1, connection.city2):
                
                if city not in self.father:
                    
                    self.father[city] = city 
                    
                    self.count += 1 
                    
        for connection in connections:
            
            if self.union(connection.city1, connection.city2):
                
                results.append(connection)
                
        if self.count == 1:
            
            return results
            
        return [] 
        
    def union(self, a, b):
        
        root_a = self.find(a)
        root_b = self.find(b)
        
        if root_a == root_b:
            
            return False 
            
        self.father[root_b] = root_a
        
        self.count -= 1 
        
        return True 
        
    def find(self, city):
        
        path = [] 
        
        while self.father[city] != city:
            
            path.append(city)
            
            city = self.father[city]
            
        for c in path:
            
            self.father[c] = city 
            
        return city 
        
        