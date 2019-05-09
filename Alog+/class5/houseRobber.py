class Solution:
    """
    @param A: An array of non-negative integers
    @return: The maximum amount of money you can rob tonight
    """
    def houseRobber(self, A):
        # write your code here
        
        n = len(A)
        
        dp = [0 for _ in range(n + 1)]
        
        i = 1
        
        for i in range(1, n + 1):
            
            if i == 1:
                dp[1] = A[0]
                
            else:
                
                dp[i] = max(dp[i - 1], dp[i - 2] + A[i - 1])
                
                
        return dp[n]