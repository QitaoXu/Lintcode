"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: the given k sorted interval lists
    @return:  the new sorted interval list
    """
    def mergeKSortedIntervalLists(self, intervals):
        # write your code here
        return self.mergeKSortedIntervalListsHelper(0 , len(intervals) - 1, intervals)
        
    def mergeKSortedIntervalListsHelper(self, start, end, intervals):
        
        if start >= end:
            
            return intervals[start]
            
        mid = (start + end) // 2 
            
        left = self.mergeKSortedIntervalListsHelper(start, mid, intervals)
        
        right = self.mergeKSortedIntervalListsHelper(mid + 1, end, intervals)
        
        return self.mergeTwoIntervals(left, right)
        
    def mergeTwoIntervals(self, list1, list2):
        
        i, j = 0, 0 
        
        curt, last = None, None 
        
        results = [] 
        
        if list1 is None or list2 is None:
            
            return results
        
        while i < len(list1) and j < len(list2):
            
            if list1[i].start < list2[j].start:
                
                curt = list1[i]
                
                i += 1 
                
            else:
                
                curt = list2[j]
                
                j += 1 
                
            last = self.merge(curt, last, results)
            
        while i < len(list1):
            
            curt = list1[i]
            
            i += 1 
            
            last = self.merge(curt, last, results)
            
        while j < len(list2):
            
            curt = list2[j]
            
            j += 1 
            
            last = self.merge(curt, last, results)
            
            
        if last is not None:
            
            results.append(last)
            
        return results 
            
            
    def merge(self, curt, last, results):
        
        if last == None:
            
            return curt 
            
        if last.end < curt.start:
            
            results.append(last)
            
            return curt 
            
        last.end = max(last.end, curt.end)
        
        return last 
        