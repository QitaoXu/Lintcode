DIRECTIONS = [
    [0, 1], [0, -1], [1, 0], [-1, 0]
]
class Solution:
    """
    @param board: the given 2D board
    @return: the number of battle ships
    """
    def countBattleships(self, board):
        # Write your code here
        
        self.father = {} 
        self.count = 0 
        
        battles = set()
        
        for x in range(len(board)):
            
            for y in range(len(board[0])):
                
                
                if board[x][y] == '.':
                    
                    continue 
                
                elif (x, y) in battles:
                    
                    continue
                
                battles.add((x, y))
                
                self.father[(x, y)] = (x, y)
                
                self.count += 1 
                
                for dx, dy in DIRECTIONS:
                    
                    nx, ny = x + dx, y + dy 
                    
                    if (nx, ny) in battles:
                        
                        self.union((x, y), (nx, ny))
                        
        return self.count 
                        
        
    def union(self, a, b):
        
        root_a = self.find(a)
        root_b = self.find(b)
        
        if root_a == root_b:
            
            return 
        
        self.father[root_b] = root_a
            
        self.count -= 1 
            
        return  
        
    def find(self, point):
        
        path = [] 
        
        while self.father[point] != point:
            
            path.append(point)
            
            point = self.father[point]
            
        for p in path:
            
            self.father[p] = point 
            
        return point 