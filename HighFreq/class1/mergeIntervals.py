"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: interval list.
    @return: A new interval list.
    """
    def merge(self, intervals):
        # write your code here
        
        intervals = sorted(intervals, key = lambda interval:interval.start)
        
        last = None 
        
        result = [] 
        
        for curt in intervals:
            
            if last == None or last.end < curt.start:
                
                result.append(curt)
                
                last = curt 
                
            else:
                
                last.end = max(last.end, curt.end)
                
        return intervals
