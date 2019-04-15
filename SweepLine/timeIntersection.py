"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param seqA: the list of intervals
    @param seqB: the list of intervals
    @return: the time periods
    """
    def timeIntersection(self, seqA, seqB):
        # Write your code here
        
        points = [] 
        
        for interval in seqA + seqB:
            
            points.append((interval.start, 1))
            points.append((interval.end, -1 ))
            
        points = sorted(points)
        
        online = 0 
        
        res = [] 
        
        last_timestamp = None 
        
        for timestamp, delta in points:
            
            if online == 2:
                
                self.merge_to(last_timestamp, timestamp, res)
                
            online += delta 
            
            last_timestamp = timestamp
            
        return res 
        
    def merge_to(self, start, end, res):
        
        if start is None or start == end:
            
            return 
        
        if res and res[-1].end == start:
            
            res[-1].end = end 
            
            return 
            
        res.append(Interval(start, end))