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
        
        for l in list2:
            
            list1 = self.insertInterval(list1, l)
            
        return list1
        
    def insertInterval(self, intervals, newInterval):
        
        index = 0 
        
        while index < len(intervals) and intervals[index].start < newInterval.start:
            index += 1 
            
        intervals.insert(index, newInterval)
        
        answer = [] 
        
        last = None 
        
        for curr in intervals:
            
            if last is None or last.end < curr.start:
                
                answer.append(curr)
                
                last = curr 
                
            else:
                
                last.end = max(last.end, curr.end)
                
        return answer