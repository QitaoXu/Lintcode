from collections import deque 

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

class Solution:
    def slidingPuzzle(self, board) -> int:
        
        m, n = len(board), len(board[0])
        
        init_state = [ ['' for _ in range(n)] for _ in range(m) ] 
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                init_state[i][j] = str(board[i][j])
        
        target_state = [['1', '2', '3'], ['4', '5', '0']]
        
        source = self.matrix_to_string(init_state)
        target = self.matrix_to_string(target_state)
        
        queue = deque()
        distance = {} 
        
        queue.append(source)
        distance[source] = 0 
        
        while queue:
            
            size = len(queue)
            
            for _ in range(size):
                
                node = queue.popleft()
                
                if node == target:
                    return distance[node]
                
                for neighbor in self.get_neighbors(node):
                    
                    if neighbor in distance:
                        continue 
                        
                    queue.append(neighbor)
                    distance[neighbor] = distance[node] + 1 
                    
        return -1 
        
    def matrix_to_string(self, matrix):
        
        m, n = len(matrix), len(matrix[0])
        
        seq = [] 
        
        for i in range(m):
            for j in range(n):
                
                seq.append(matrix[i][j])
                
        return "".join(seq)
    
    def get_neighbors(self, state):
        
        zeroIndex = state.find('0')
        
        x, y = zeroIndex // 3, zeroIndex % 3 
        
        neighbors = [] 
        
        for dx, dy in DIRECTIONS:
            
            seq = list(state)
            
            nx, ny = x + dx, y + dy 
            
            if nx < 0 or nx >= 2 or ny < 0 or ny >= 3:
                continue 
                
            seq[zeroIndex], seq[nx * 3 + ny] = seq[nx * 3 + ny], seq[zeroIndex]
            
            neighbor = "".join(seq)
            neighbors.append(neighbor)
            
        return neighbors
                
            
        
        