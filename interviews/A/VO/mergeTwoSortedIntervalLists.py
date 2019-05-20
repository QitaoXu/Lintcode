"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param list1: one of the given list
    @param list2: another list
    @return: the new sorted list of interval
    """
    def mergeTwoInterval(self, list1, list2):
        # write your code here
        
        i, j = 0, 0 
        intervals = [] 
        
        while i < len(list1) and j < len(list2):
            
            if list1[i].start < list2[j].start:
                self.pushback(intervals, list1[i])
                i += 1 
                
            else:
                self.pushback(intervals, list2[j])
                j += 1 
                
        while i < len(list1):
            self.pushback(intervals, list1[i])
            i += 1 
            
        while j < len(list2):
            self.pushback(intervals, list2[j])
            j += 1 
            
        return intervals
        
    def pushback(self, intervals, interval):
        
        if not intervals:
            intervals.append(interval)
            return 
        
        if intervals[-1].end < interval.start:
            intervals.append(interval)
            
            return 
        
        intervals[-1].end = max(intervals[-1].end, interval.end)
