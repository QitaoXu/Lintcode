from collections import deque

class Solution:
    """
    @param pid: the process id
    @param ppid: the parent process id
    @param kill: a PID you want to kill
    @return: a list of PIDs of processes that will be killed in the end
    """
    def killProcess(self, pid, ppid, kill):
        # Write your code here
        
        graph = {}
        
        for process in pid:
            
            graph[process] = []
        
        for i, parent in enumerate(ppid):
            
            if parent == 0:
                continue 
            
            if parent not in graph:
                graph[parent] = []
                
            graph[parent].append(pid[i])
            
        queue = deque()
        seen = set()
        
        queue.append(kill)
        seen.add(kill)
        
        answer = []
        
        while queue:
            
            node = queue.popleft()
            
            answer.append(node)
            
            for neighbor in graph[node]:
                
                if neighbor in seen:
                    
                    continue 
                
                queue.append(neighbor)
                
                seen.add(neighbor)
                
        return answer
