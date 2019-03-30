class Solution:
    """
    @param numbers: Give an array
    @param target: An integer
    @return: Find all unique quadruplets in the array which gives the sum of zero
    """
    def fourSum(self, numbers, target):
        # write your code here
        
        nums = numbers
        
        results = [] 
        
        if nums == None or len(nums) < 4:
            return results 
            
        nums.sort()
            
        for i in range(0, len(nums) - 3):
            
            if i and nums[i] == nums[i - 1]:
                continue 
            
            for j in range(i + 1, len(nums) - 2):
                
                if (j - 1) > i and nums[j] == nums[j - 1]:
                    continue 
                
                left, right = j + 1, len(nums) - 1 
                
                half_target = target - nums[i] - nums[j]
                
                while left < right:
                    
                    if nums[left] + nums[right] < half_target:
                        left += 1 
                        
                    elif nums[left] + nums[right] == half_target:
                        results.append( [ nums[i], nums[j], nums[left], nums[right] ] )
                        
                        left += 1 
                        right -= 1 
                        
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1 
                        
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1 
                        
                    elif nums[left] + nums[right] > half_target:
                        right -= 1 
                        
        return results