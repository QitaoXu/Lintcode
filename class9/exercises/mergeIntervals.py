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
        
        intervals = sorted(intervals, key = lambda i:i.start)
        
        last = None 
        
        result = []
        
        for curr in intervals:
            
            if last is None or last.end < curr.start:
                
                result.append(curr)
                last = curr
                
            else:
                
                last.end = max(last.end, curr.end)
                
        return result