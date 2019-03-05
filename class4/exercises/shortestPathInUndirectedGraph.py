from collections import deque

class Solution:
    """
    @param graph: a list of Undirected graph node
    @param A: nodeA
    @param B: nodeB
    @return:  the length of the shortest path
    """
    def shortestPath(self, graph, A, B):
        # Write your code here
        
        start, end = A, B 
        
        if start == end:
            return 0 
        
        startQueue, endQueue = deque(), deque() 
        startSeen, endSeen = set(), set() 
        
        startQueue.append(start)
        startSeen.add(start) 
        
        endQueue.append(end)
        endSeen.add(end) 
        
        step = 0 
        
        while len(startQueue) and len(endQueue):
            
            startSize, endSize = len(startQueue), len(endQueue)
            
            step += 1 
            
            for _ in range(startSize):
                
                curr = startQueue.popleft()
                
                for neighbor in curr.neighbors:
                    
                    if neighbor in startSeen:
                        continue 
                    
                    elif neighbor in endSeen:
                        return step 
                        
                    else:
                        startQueue.append(neighbor)
                        startSeen.add(neighbor)
                        
            step += 1 
            
            for _ in range(endSize):
                
                curr = endQueue.popleft() 
                
                for neighbor in curr.neighbors:
                    
                    if neighbor in endSeen:
                        continue 
                    
                    elif neighbor in startSeen: 
                        return step 
                        
                    else:
                        endQueue.append(neighbor)
                        endSeen.add(neighbor)
                        
        
        return -1 