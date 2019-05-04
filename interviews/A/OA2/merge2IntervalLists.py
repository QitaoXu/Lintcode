"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

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
                
                self.push_back(intervals, list1[i])
                
                i += 1 
                
            else:
                
                self.push_back(intervals, list2[j])
                
                j += 1 
                
        while i < len(list1):
            
            self.push_back(intervals, list1[i])
            
            i += 1 
            
        while j < len(list2):
            
            self.push_back(intervals, list2[j])
            
            j += 1 
            
        return intervals
        
    def push_back(self, intervals, interval):
        
        if not intervals:
            
            intervals.append(interval)
            
        if intervals[-1].end < interval.start:
            
            intervals.append(interval)
            
            return
            
        intervals[-1].end = max(intervals[-1].end, interval.end)

intervals1 = [Interval(1, 2),Interval(3, 4)]
intervals2 = [Interval(2, 3),Interval(5, 10)]

solution = Solution()

intervals = solution.mergeTwoInterval(intervals1, intervals2)
for interval in intervals:
    print(interval.start, interval.end)

intervals = sorted(intervals, key = lambda interval : (interval.end - interval.start, interval.start), reverse = True)
for interval in intervals:
    print(interval.start, interval.end)
