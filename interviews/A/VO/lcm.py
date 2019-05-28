class Solution:

    def lcm(self, nums):

        lcm = nums[0]

        for num in nums[1:]:

            lcm = lcm * num // self.gcd(lcm, num)

        return lcm 

    def gcd(self, a, b):

        if a < b:
            return self.gcdHelper(a, b)

        else:

            return self.gcdHelper(b, a)

    def gcdHelper(self, small, big):

        if big % small == 0:
            return small 

        return self.gcdHelper(big % small, small)

solution = Solution()
nums = [2, 3, 4]

print(solution.lcm(nums))