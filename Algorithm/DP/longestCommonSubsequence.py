class Solution:
    """
    @param A: A string
    @param B: A string
    @return: The length of longest common subsequence of A and B
    """
    def longestCommonSubsequence(self, A, B):
        # write your code here
            
        return self.lcs_helper(A, B, len(A), len(B), {})
        
    def lcs_helper(self, A, B, m, n, memo):
        
        if (m, n) in memo:
            
            return memo[(m, n)]
            
        if m == 0 or n == 0:
            
            result = 0 
            
        elif A[m - 1] == B[n - 1]:
            
            result = 1 + self.lcs_helper(A, B, m - 1, n - 1, memo)
            
        else:
            
            result = max(self.lcs_helper(A, B, m - 1, n, memo), 
                        self.lcs_helper(A, B, m, n - 1, memo) )
                        
        memo[(m, n)] = result
        
        return result

class Solution2:
    """
    @param A: A string
    @param B: A string
    @return: The length of longest common subsequence of A and B
    """
    def longestCommonSubsequence(self, A, B):
        # write your code here
        
        n, m = len(A), len(B)
        
        dp = [[0] * (n + 1) for i in range(m + 1)]
        
        for i in range(1, m + 1):
            
            for j in range(1, n + 1):
                
                if B[i - 1] == A[j - 1]:
                    
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                    
                else:
                    
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                    
        return dp[m][n]