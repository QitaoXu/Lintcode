from collections import deque
class Solution:
    def removeInvalidParentheses(self, s):
        results = [] 
        
        if self.is_valid(s):
            
            results.append(s)
            
            return results
        
        queue = deque()
        
        visited = set()
        
        queue.append(s)
        
        visited.add(s)
        
        while queue:
            
            size = len(queue) 
            
            if results:
                
                return results
            
            for _ in range(size):
                
                node = queue.popleft()
                
                for neighbor in self.get_neighbors(node):
                    
                    if neighbor in visited:
                        
                        continue 
                    
                    if self.is_valid(neighbor):
                        
                        results.append(neighbor)
                        
                    queue.append(neighbor)
                    visited.add(neighbor)
                    
        return results
            
            
            
    def get_neighbors(self, s):
        
        neighbors = [] 
        
        for i in range(0, len(s)):
            
           neighbor = s[:i] + s[i + 1:]
           
           neighbors.append(neighbor)
           
        return neighbors 
            
        
    def is_valid(self, s):
        
        stack = [] 
        
        for c in s:
            
            if c == '(':
                
                stack.append(c)
                
            elif c == ')':
                
                if not stack:
                    
                    return False 
                    
                stack.pop()
                
            else:
                
                continue 
        
        return len(stack) == 0