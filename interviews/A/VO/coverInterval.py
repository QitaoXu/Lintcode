class Solution:

    def coverInnterval(self, intervals):

        if not intervals:
            return 0 

        intervals = sorted(intervals, key = lambda interval : (interval[0], interval[1]))

        results = [intervals[0]] 

        last = intervals[0] 

        for interval in intervals:

            if last[0] <= interval[0] and last[1] >= interval[1]:

                continue 

            else:

                results.append(interval)
                last = interval 

        return len(results)



solution = Solution()

intervals = [[1,4],[3,6],[2,8]]

print(solution.coverInnterval(intervals))

                
            

