class Solution:
    """
    @param nums: the sorted matrix
    @return: the number of Negative Number
    """
    def countNumber(self, nums):
        # Write your code here
        
        m, n = len(nums), len(nums[0])
        
        x, y = m - 1, 0 
        
        count = 0 
        
        while x >= 0 and y < n:
            
            if nums[x][y] > 0:
                
                x -= 1 
                
            elif nums[x][y] == 0:
                
                count += x
                
                y += 1 
                
                x -= 1 
                
            elif nums[x][y] < 0:
                
                count += x + 1 
                
                y += 1 
                
        return count 