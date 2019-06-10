class Solution:
    def findPairs(self, nums, k):
        
        n, i, j = len(nums), 0, 0 
        nums.sort()
        ans = 0 
        
        while i < n:
            
            if i == j:
                j += 1 
                
            while i + 1 < n and nums[i] == nums[i + 1]:
                i += 1 
                
            while j + 1 < n and nums[j] == nums[j + 1]:
                j += 1 
                
            while j < n and abs(nums[j] - nums[i]) < k:
                j += 1 
                
            if j >= n:
                break 
                
            if abs(nums[j] - nums[i]) == k:
                ans, j = ans + 1, j + 1
                
            i += 1 
                
        return ans 
                
class Solution2:
    def findPairs(self, nums, k):
        
        count = 0
        
        if k < 0:
            return count 
        
        elif k == 0:
            
            num_to_count = {} 
            for num in nums:
                
                num_to_count[num] = num_to_count.get(num, 0) + 1 
                
                if num_to_count[num] == 2:
                    
                    count += 1 
                    
            return count 
        
        else:
            nums = set(nums)
        
            for num in nums:
                if num + k in nums:
                    count += 1 
                
            return count         
        