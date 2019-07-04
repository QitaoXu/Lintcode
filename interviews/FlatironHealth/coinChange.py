import sys 
class Solution:
    
    def coinChange(self, coins, amount):
        
        dp = [sys.maxsize for _ in range(amount + 1)]
        
        dp[0] = 0 
        
        for i in range(1, amount + 1):
            for coin in coins: 
                
                if coin <= i: 
                    
                    dp[i] = min(dp[i - coin] + 1, dp[i])
                    
        return -1 if dp[amount] == sys.maxsize else dp[amount]