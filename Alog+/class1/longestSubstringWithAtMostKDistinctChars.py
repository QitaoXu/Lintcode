#
# Solution1
#
class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def lengthOfLongestSubstringKDistinct(self, s, k):
        # write your code here
        
        left, right = 0, 0 
        
        char_count = [0 for _ in range(256)]
        
        key_count = 0
        
        ans = 0 
        
        n = len(s)
        
        for left in range(n):
            
            while right < n and key_count <= k:
                
                if char_count[ord(s[right])] == 0:
                    
                    key_count += 1 
                    
                if key_count > k:
                    
                    key_count -= 1 
                    break
                
                char_count[ord(s[right])] += 1 
                
                right += 1 
                
            ans = max(ans, min(right - left, n))
            
            char_count[ord(s[left])] -= 1 
            
            if char_count[ord(s[left])] == 0:
                
                key_count -= 1 
                
        return ans
    
#   
# Solution2 
#
class Solution2:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def lengthOfLongestSubstringKDistinct(self, s, k):                
        
        if not s:
            
            return 0
        
        left = 0 
        
        n = len(s)
        
        count = [0 for _ in range(256)]
        
        key_count = 0 
        
        ans = 0
        
        for right in range(n):
            
            count[ ord(s[right]) ] += 1 
            
            if count[ ord(s[right]) ] == 1:
                
                key_count += 1  
                
            while key_count > k:
                
                count[ord(s[left])] -= 1 
                
                if count[ord(s[left])] == 0:
                    
                    key_count -= 1 
                    
                left += 1  
                
            ans = max(ans, right - left + 1)
            
        return ans