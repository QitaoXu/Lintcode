class Solution:
    """
    @param num: a non-negative intege
    @return: the maximum valued number
    """
    def maximumSwap(self, num):
        # Write your code here
        
        res, nums = num, list(str(num))
        
        for i in range(len(nums) - 1):
            
            for j in range(i + 1, len(nums)):
                
                if int(nums[j]) > int(nums[i]):
                    
                    temp = int("".join( nums[0 : i] + [nums[j]] + nums[i + 1 : j] + [nums[i]] + nums[j + 1:]))
                    
                    res = max(temp, res)
                    
        return res 
            
        
