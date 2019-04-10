class Solution:
    """
    @param num: A list of integers
    @return: An integer
    """
    def longestConsecutive(self, num):
        # write your code here
        
        hashset = set(num)
        
        ans = 0 
        
        for n in num:
            
            if n in hashset:
                
                length = 1 
                
                left = n - 1 
                
                while left in hashset:
                    
                    length += 1 
                    
                    hashset.remove(left)
                    
                    left -= 1 
                    
                right = n + 1 
                
                while right in hashset:
                    
                    length += 1 
                    
                    hashset.remove(right)
                    
                    right += 1 
                    
                ans = max(ans, length)
                
        return ans 