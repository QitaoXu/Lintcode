class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        # write your code here
        
        nums = numbers 
        diff = sys.maxsize 
        three_sum = 0 
        result = 0
        
        if nums == None or len(nums) == 0:
            return None 
            
        nums.sort() 
        
        for i in range(0, len(nums) - 2):
            
            left, right = i + 1, len(nums) - 1 
            
            # _target = target - nums[i]
            
            while left < right:
                
                three_sum = nums[i] + nums[left] + nums[right]
                
                if three_sum < target:
                    if diff > target - three_sum:
                        diff = target - three_sum
                        result = three_sum
                    
                    left += 1 
                    
                elif three_sum == target:
                    return target 
                    
                elif three_sum > target:
                    if diff > three_sum - target:
                        diff = three_sum - target 
                        result = three_sum
                    
                    right -= 1 
                    
        return result