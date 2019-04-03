class Solution:
    """
    @param timePoints: a list of 24-hour clock time points
    @return: the minimum minutes difference between any two time points in the list
    """
    def findMinDifference(self, timePoints):
        # Write your code here
        if not timePoints or len(timePoints) == 1:
            
            return None
        
        time = []
        
        for timePoint in timePoints:
            
            hour_and_minute = timePoint.split(":")
            
            time.append([int(hour_and_minute[0]), int(hour_and_minute[1])])
            
        time = sorted(time)
        
        min_diff = 24 * 60 
        
        for i in range(0, len(time) - 1):
            
            diff = self.time_diff(time[i], time[i + 1])
            
            min_diff = min(min_diff, diff)
        
        min_diff = min(min_diff, 24 * 60 - self.time_diff(time[0], time[-1]))
        
        return min_diff
            
    def time_diff(self, t1, t2):
        
        res = t2[0] * 60 - t1[0] * 60
        
        if t2[1] > t1[1]:
            
            res += t2[1] - t1[1]
            
        else:
            
            res -= t1[1] - t2[1]
            
        return res 