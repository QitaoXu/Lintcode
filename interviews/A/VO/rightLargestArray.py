class Solution:

    def changeToRightLargest(self, nums):

        print(nums)

        curt_max = nums[-1]

        for i in range(len(nums) - 1, -1, -1):

            if nums[i] <= curt_max:

                nums[i] = curt_max

            else:

                nums[i], curt_max = curt_max, nums[i]

        return nums 

solution = Solution()
nums = [2, 1, 5, 2, 1]

print(solution.changeToRightLargest(nums))