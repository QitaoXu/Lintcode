import sys 
class Solution: 

    def minIntersectionToFormAPalin(self, string):

        # return self.helper(string, 0, len(string) - 1, {}) 

        lcs = self.lcs(string, string[::-1]) 
        print(lcs)

        return len(string) - lcs 

    def helper(self, string, l, r, memo):

        substring = string[l : r + 1]

        if substring in memo:
            return memo[substring]  

        if l > r: 
            return sys.maxsize

        if l == r:
            memo[substring] = 0
            return memo[substring]

        if l == r - 1:
            memo[substring] = 0 if string[l] == string[r] else 1 
            return memo[substring] 
        
        if string[l] == string[r]:

            memo[substring] = self.helper(string, l + 1, r - 1, memo) 

        else:
            memo[substring] = min(self.helper(string, l, r - 1, memo), self.helper(string, l + 1, r, memo)) + 1 

        return memo[substring]

    def lcs(self, s1, s2):

        m, n = len(s1), len(s2) 

        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)] 

        for i in range(1, m + 1):
            for j in range(1, n + 1):

                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1 

                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) 

        return dp[m][n] 

solution = Solution()

print(solution.minIntersectionToFormAPalin("geeks")) 