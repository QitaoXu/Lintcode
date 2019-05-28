class Solution:

    def reverseString(self, s):

        if not s:
            return 

        return self.reverseStringHelper(s, 0, len(s) - 1)

    def reverseStringHelper(self, s, start, end):

        if start >= end:
            return s[start]

        mid = start + (end - start) // 2 

        left = self.reverseStringHelper(s, start, mid)
        right = self.reverseStringHelper(s, mid + 1, end)

        return right + left 

solution = Solution()

s = "abcde"

print(solution.reverseString(s))