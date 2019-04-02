import sys
class Solution:

    def subarraySumClosestK(self, nums, k):

        if not nums:

            return sys.maxsize, -1, -1

        prefix_sum = 0 

        prefix_sum_list = []

        prefix_sum_list.append(0)

        for i in range(len(nums)):

            prefix_sum += nums[i]

            prefix_sum_list.append(prefix_sum)

        min_diff = sys.maxsize 

        min_left, min_right = -1, -1 

        for i in range(len(prefix_sum_list) - 1):

            for j in range(i + 1, len(prefix_sum_list)):

                range_sum = prefix_sum_list[j] - prefix_sum_list[i]

                diff = abs(k - range_sum)

                if diff < min_diff:

                    min_diff = diff 
                    min_left, min_right = i, j - 1 

        return min_diff, min_left, min_right


solution = Solution()

nums = [2, 0, 5, 6, 5, -1, -3, 2, 2]

min_diff, left_index, right_index = solution.subarraySumClosestK(nums, 3)

print("nums: ", nums)
index_range = [ _ for _ in range(len(nums))]
print("index: ", index_range)
print("range: ", [left_index, right_index])

