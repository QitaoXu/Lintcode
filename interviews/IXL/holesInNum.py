ZERO = set([1, 3, 5, 7])
ONE = set([0, 2, 4, 6])
# TWO = set([8])

class Solution:

    def findHolesInNum(self, nums):

        res = [] 

        if not nums:
            return res 

        for num in nums:
            res.append(self.getHoleInNum(num))

        return res 

    def getHoleInNum(self, num):

        if num == 0:
            return 1 

        holes = 0 

        while num > 0:

            digit = num % 10 

            if digit in ZERO:
                hole = 0 

            elif digit in ONE:
                hole = 1 

            else:
                hole = 2 

            holes += hole 
            num = num // 10 

        return holes 

solution = Solution()

nums = [12, 67, 812, 0]

print(solution.findHolesInNum(nums))