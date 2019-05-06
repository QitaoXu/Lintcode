from heapq import heappush, heappop
class Solution:

    def firstDupIndexInUnsortedArray(self, nums):

        if not nums:
            return -1 

        num_to_index = {}
        dup_index = [] 

        for i in range(len(nums)):

            if nums[i] not in num_to_index:
                num_to_index[nums[i]] = i 

            else:
                heappush(dup_index, num_to_index[nums[i]])

        return dup_index[0] if dup_index else -1 

solution = Solution()

nums = [43, 41, 3, 2, -9, 3, 4, 5, 8, 43]

print(solution.firstDupIndexInUnsortedArray(nums))