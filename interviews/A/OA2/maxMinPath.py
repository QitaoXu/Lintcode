class Solution:

    def maxiumMinimumPath1(self, matrix):

        if not matrix or not matrix[0]:
            return 0 

        m, n = len(matrix), len(matrix[0])

        dp = [[0 for _ in range(n)] for _ in range(m)]

        dp[0][0] = matrix[0][0]

        for i in range(1, m):
            
            dp[i][0] = min(dp[i - 1][0], matrix[i][0])

        for j in range(1, n):

            dp[0][j] = min(dp[0][j - 1], matrix[0][j])

        for i in range(1, m):
            for j in range(1, n):

                dp[i][j] = max( min(dp[i - 1][j], matrix[i][j]), min(dp[i][j - 1], matrix[i][j]) )

        return dp

matrix = [[2, 2, 3], [3, 2, 1], [2, 1, 1]]

solution = Solution()

for row in matrix:
    print(row)

print(solution.maxiumMinimumPath1(matrix))