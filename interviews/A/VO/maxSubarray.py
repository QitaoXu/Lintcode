class Solution:

    def maxSubarray(self, nums):

        start, end = 0, 0 

        min_prefixsum = 0
        max_subarray_sum = - 2 ** 31 

        n = len(nums)

        prefix_sum = [0]

        for i in range(1, n + 1):

            prefix_sum.append(prefix_sum[-1] + nums[i - 1])

            if prefix_sum[i] - min_prefixsum > max_subarray_sum:
                max_subarray_sum = prefix_sum[i] - min_prefixsum
                end = i - 1 

            if prefix_sum[i] < min_prefixsum:
                min_prefixsum = prefix_sum[i]
                start = i


        return (start, end), max_subarray_sum 

solution = Solution()

nums = [-2,2,-3,4,-1,2,1,-5,3] 

print(nums)

print(solution.maxSubarray(nums))