from heapq import heappop, heappush 

DIRECTIONS = [
    [0, 1], [1, 0], [0, -1], [-1, 0]
]
    
class Solution:
    """
    @param heights: a matrix of integers
    @return: an integer
    """
    def trapRainWater(self, heights):
        # write your code here
        
        if not heights:
            
            return 0
        
        self.initialize(heights)
        
        water = 0
        
        while self.heap:
            
            height, x, y = heappop(self.heap)
            
            for nx, ny in self.get_neighbors(x, y):
                
                water += max(height - heights[nx][ny], 0)
                
                self.add(max(heights[nx][ny], height), nx, ny)
                
        return water 
        
    def initialize(self, heights):
        
        self.m = len(heights)
        self.n = len(heights[0])
        
        self.visited = set()
        self.heap = [] 
        
        for index in range(self.m):
            
            self.add(heights[index][0], index, 0)
            self.add(heights[index][self.n - 1], index, self.n - 1)
            
        for index in range(self.n):
            
            self.add(heights[0][index], 0, index)
            self.add(heights[self.m - 1][index], self.m - 1, index)
            
    def add(self, height, x, y):
        
        if (x, y) in self.visited:
            
            return 
        
        heappush(self.heap, (height, x, y))
        self.visited.add((x, y))
        
    def get_neighbors(self, x, y):
        
        neighbors = [] 
        
        for dx, dy in DIRECTIONS:
            
            nx, ny = x + dx, y + dy 
            
            if nx < 0 or nx >= self.m or ny < 0 or ny >= self.n:
                
                continue 
            
            if (nx, ny) in self.visited:
                
                continue
            
            neighbors.append((nx, ny))
            
        return neighbors
        
            
            
        
        
