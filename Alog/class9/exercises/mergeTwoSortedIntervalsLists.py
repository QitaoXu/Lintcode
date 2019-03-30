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
        
        results = []
        
        
        if list1 is None and  list2 is None:
            
            return results 
            
        curt, last = None, None
            
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
            
            last = self.merge(curt, last, results)
            
            i += 1 
            
        while j < len(list2):
            
            curt = list2[j]
            
            last = self.merge(curt, last, results)
            
            j += 1 
            
        if last is not None:
            
            results.append(last)
            
        return results
            
            
        
    def merge(self, curt, last, results):
        
        if last is None:
            
            return curt 
            
        if last.end < curt.start:
            
            results.append(last)
            
            return curt 
            
        last.end = max(last.end, curt.end)
        
        return last 