"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        # Write your code here
        
        if not intervals:
            
            return 0 
        
        points = []
        
        for interval in intervals:
            
            points.append((interval.start, 1))
            points.append((interval.end, -1))
            
        points = sorted(points)
        
        max_count = 0 
        
        curt_count = 0
        
        for _, delta in points:
            
            curt_count += delta
            
            max_count = max(curt_count, max_count)
            
        return max_count
            
            
