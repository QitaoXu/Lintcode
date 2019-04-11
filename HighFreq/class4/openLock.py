from collections import deque 

class Solution:
    """
    @param deadends: the list of deadends
    @param target: the value of the wheels that will unlock the lock
    @return: the minimum total number of turns 
    """
    def openLock(self, deadends, target):
        # Write your code here
        deadends_set = set(deadends)
        
        start = "0000"
        
        if start in deadends_set:
            
            return -1 

        queue = deque()
        distance = {}
        
        queue.append(start)
        distance[start] = 0 

        while queue:
            
            size = len(queue)
            
            for _ in range(size):
                
                current = queue.popleft()
                
                if current == target:
                    
                    return distance[current]
                
                for neighbor in self.get_neighbors(current, deadends_set):
                    
                    if neighbor in distance:
                        
                        continue
                    
                    queue.append(neighbor)
                    distance[neighbor] = distance[current] + 1 
                    
        return -1 
        
        
    def get_neighbors(self, current, deadends):
        
        neighbors = [] 
        
        for i in range(len(current)):
            
            left, mid, right = current[:i], current[i], current[i + 1:]
            
            for digit in [(int(mid) + 1) % 10, (int(mid) - 1) % 10]:
                
                neighbor = left + str(digit) + right 
                
                if neighbor in deadends:
                    
                    continue 
                
                neighbors.append(neighbor)
                
        return neighbors