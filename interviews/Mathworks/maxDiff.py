class Solution:

    def findMaxDiff(self, nums):

        lessThanMin = [0 for _ in range(len(nums))]

        min_val = nums[0] 

        for i in range(1, len(nums)):

            if nums[i] > min_val:
                lessThanMin[i] = min_val

            elif nums[i] == min_val:
                lessThanMin[i] = -1 

            else:

                lessThanMin[i] = -1 
                min_val = nums[i]

        max_diff = -1 

        for i in range(1, len(nums)):

            if lessThanMin[i] == -1:
                continue 

            else:
                diff = nums[i] - lessThanMin[i]
                max_diff = max(diff, max_diff)

        return max_diff

# nums = [1, 2, 6, 4]
# nums = [1]
nums = [4, 3, 2, 1]
solution = Solution()

print(solution.findMaxDiff(nums))