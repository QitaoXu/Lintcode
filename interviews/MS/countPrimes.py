class Solution:
    """
    @param n: a integer
    @return: return a integer
    """
    def countPrimes(self, n):
        # write your code here
        
        if n <= 1:
            
            return 0 
            
        not_prime = [False] * n 
        
        count = 0 
        
        for i in range(2, n):
            
            if not_prime[i] == False:
                
                count += 1 
                
                for j in range(2, n):
                    
                    if i * j >= n:
                        
                        break 
                    
                    not_prime[i * j] = True 
                    
        return count 