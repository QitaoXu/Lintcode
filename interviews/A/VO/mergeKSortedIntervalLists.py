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
        
        # Solution 1: Divide Conquer
        # return self.mergeKSortedIntervalListsHelper(0 , len(intervals) - 1, intervals)
        
        # Solution 2: Merge 2 by 2 
        
        return self.merge_2_by_2(intervals)
        
    def mergeKSortedIntervalListsHelper(self, start, end, intervals):
        
        if start >= end:
            
            return intervals[start]
            
        mid = (start + end) // 2 
            
        left = self.mergeKSortedIntervalListsHelper(start, mid, intervals)
        
        right = self.mergeKSortedIntervalListsHelper(mid + 1, end, intervals)
        
        return self.mergeTwoIntervals(left, right)
        
    def mergeTwoIntervals(self, list1, list2):
        
        i, j = 0, 0 
        
        res = [] 
        
        while i < len(list1) and j < len(list2):
            
            if list1[i].start < list2[j].start:
                
                self.pushBack(res, list1[i])
                i += 1 
                
            else:
                
                self.pushBack(res, list2[j])
                j += 1  
                
        while i < len(list1):
            self.pushBack(res, list1[i])
            i += 1 
            
        while j < len(list2):
            self.pushBack(res, list2[j])
            j += 1 
            
        return  res 
        
    def pushBack(self, res, interval):
        
        if not res:
            res.append(interval)
            return 
        
        if res[-1].end < interval.start:
            res.append(interval)
            
            return 
        
        res[-1].end = max(res[-1].end, interval.end)
            
            
    def merge_2_by_2(self, interval_lists):
        
        while len(interval_lists) > 1:
            
            new_interval_lists = [] 
            
            for i in range(0, len(interval_lists), 2):
                
                if i + 1 >= len(interval_lists):
                    break 
                
                new_interval_list = self.mergeTwoIntervals(interval_lists[i], interval_lists[i + 1])
                new_interval_lists.append(new_interval_list)
                
            if len(interval_lists) % 2 == 1:
                
                new_interval_lists.append(interval_lists[-1])
                
            interval_lists = new_interval_lists
                
        return new_interval_lists[0]
        
    
       
        
        
        
        
        
        
        