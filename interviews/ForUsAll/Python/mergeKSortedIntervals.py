class Solution:

    def mergeKSortedIntervalLists(self, intervalLists):

        if not intervalLists or not intervalLists[0]:
            return [] 

        return self.helper(intervalLists, 0, len(intervalLists) - 1) 

    def helper(self, intervalLists, start, end):

        if start >= end:
            return intervalLists[start] 

        mid = start + (end - start) // 2 

        left = self.helper(intervalLists, start, mid)
        right = self.helper(intervalLists, mid + 1, end) 

        return self.merge2SortedIntervalLists(left, right) 

    def merge2SortedIntervalLists(self, intervals1, intervals2):

        i, j = 0, 0 

        results = [] 

        while i < len(intervals1) and j < len(intervals2):

            if intervals1[i].start < intervals2[j].start:

                self.pushBack(results, intervals1[i])

                i += 1 

            else:

                self.pushBack(results, intervals2[j])
                j += 1 

        while i < len(intervals1):

            self.pushBack(results, intervals1[i]) 
            i += 1 

        while j < len(intervals2):

            self.pushBack(results, intervals2[j])

            j += 1 

        return results 

    def pushBack(self, results, interval): 

        if not results:
            results.append(interval) 
            return 

        if results[-1].end < interval.start:
            results.append(interval) 
            return 

        results[-1].end = max(results[-1].end, interval.end) 

