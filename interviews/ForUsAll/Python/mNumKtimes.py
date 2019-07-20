class Solution: 

    def findNumbersDiff(self, nums, m, k): 

        mod_to_lists = {} 

        for num in nums:

            if (num % k) not in mod_to_lists:
                mod_to_lists[num % k] = [] 

            mod_to_lists[num % k].append(num) 

        for mod in mod_to_lists:
            if len(mod_to_lists[mod]) == m: 

                return mod_to_lists[mod] 

        return []  

solution = Solution()
nums = [4, 6, 8, 9]
m = 3 
k = 2 

print(solution.findNumbersDiff(nums, m, k)) 