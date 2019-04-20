from collections import deque 

DIRECTIONS = [(-1, 0), (1, 0), (0, 1), (0, - 1)]

class Node:
    
    def __init__(self, x, y, h):
        
        self.x = x 
        self.y = y  
        self.h = h 
        
    def __lt__(self, other):
        
        return self.h < other.h 

class Solution:
    """
    @param forest: a list of integers
    @return: return a integer
    """
    def cutOffTree(self, forest):
        # write your code here
        
        if not forest or not forest[0]:
            
            return 0 
            
        m, n = len(forest), len(forest[0])
            
        trees = [] 
        
        for i in range(m):
            for j in range(n):
                if forest[i][j] > 1:
                    trees.append(Node(i, j, forest[i][j]))
                    
        trees.sort()
        
        total = 0 
        start = Node(0, 0, forest[0][0])
        
        while trees:
            
            tree = trees[0]
            del trees[0]
            
            step = self.minStep(forest, start, tree, m, n)
            
            if step < 0:
                return -1 
                
            total += step 
            start = tree 
            
        return total 
        
    def minStep(self, forest, start, tree, m, n):
        
        queue = deque()
        seen = set()
        
        queue.append(start)
        seen.add((start.x, start.y))
        
        step = -1 
        
        while queue:
            
            size = len(queue) 
            step += 1 
            
            for _ in range(size):
                
                node = queue.popleft()
                
                if node.x == tree.x and node.y == tree.y:
                    return step 
                
                for dx, dy in DIRECTIONS:
                    
                    nx, ny = node.x + dx, node.y + dy
                    
                    if not self.is_valid(forest, nx, ny):
                        continue 
                    
                    if (nx, ny) in seen:
                        continue 
                    
                    queue.append(Node(nx, ny, forest[nx][ny]))
                    seen.add((nx, ny))
                    
        return -1 
        
    def is_valid(self, forest, x, y):
        
        m, n = len(forest), len(forest[0])
        
        if x < 0 or x >= m or y < 0 or y >= n:
            return False 
            
        if forest[x][y] == 0:
            return False 
            
        return True 
        