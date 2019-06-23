class Solution:

    def findBestMeetingLocation(self, clients):

        if not clients or not clients[0]:
            return 0 

        rows = self.get_rows(clients) 
        cols = self.get_cols(clients) 

        row = self.quick_select(rows, 0, len(rows) - 1, len(rows) // 2) 
        col = self.quick_select(cols, 0, len(cols) - 1, len(cols) // 2) 

        return self.get_min_distance_1d(rows, row) + self.get_min_distance_1d(cols, col) 

    def get_min_distance_1d(self, points, origin):

        distance = 0 

        for point in points:

            distance += abs(point - origin)

        return distance 

    def get_rows(self, clients):

        rows = [] 

        for (x, _) in clients:

            rows.append(x) 

        return rows 

    def get_cols(self, clients):

        cols = [] 

        for (_, y) in clients:

            cols.append(y) 

        return cols 

    def quick_select(self, nums, start, end, k):

        if start >= end:

            return nums[start] 

        left, right = start, end 

        pivot = nums[start + (end - start) // 2]

        while left <= right:

            while left <= right and nums[left] < pivot:
                left += 1 

            while left <= right and nums[right] > pivot:
                right -= 1 

            if left <= right:

                nums[left], nums[right] = nums[right], nums[left] 
                left += 1 
                right -= 1 

        if start + k - 1 <= right:

            return self.quick_select(nums, start, right, k) 

        elif start + k - 1 >= left:

            return self.quick_select(nums, left, end, k - (left - start)) 

        else:

            return nums[right + 1] 


solution = Solution() 

# clients = [[1, 0], [1, 1]] 
clients = [[-4, 3], [-2, 1], [1, 0], [3, 2]] 

print(solution.findBestMeetingLocation(clients)) 

            