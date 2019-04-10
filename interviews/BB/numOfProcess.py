"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param logs: Sequence of processes
    @param queries: Sequence of queries
    @return: Return the number of processes
    """
    def numberOfProcesses(self, logs, queries):
        # Write your code here
        
        time = [] 
        
        for log in logs:
            
            time.append((log.start, 0))
            time.append((log.end + 1, 1))
            
        for query in queries:
            
            time.append((query, 2))
            
        time = sorted(time, key = lambda t:t[0])
        
        count = 0
        
        time_to_count = {}
        
        for t, status in time:
            
            if status == 0:
                
                count += 1 
                
            elif status == 1:
                
                count -= 1 
                
            time_to_count[t] = count
            
        return [time_to_count[query] for query in queries]
                
        
                
                
                
                
            
            
