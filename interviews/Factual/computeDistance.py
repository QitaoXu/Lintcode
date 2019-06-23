class Solution:

    def computeDistance(self, readings, end_time):
        
        distance = 0 

        if not readings or not readings[0]:
            return distance 

        last_speed = readings[-1][1] 

        readings.append((end_time, last_speed)) 

        for i in range(1, len(readings)):

            start_time = readings[i - 1][0] 
            end_time = readings[i][0] 

            speed = readings[i - 1][1] 

            distance += speed * (end_time - start_time) / 3600 

        return round(distance, 2) 

# readings = [[0, 90], [300, 80]] 
readings = [[0, 90]] 
end_time = 600 

solution = Solution()

print(solution.computeDistance(readings, end_time)) 