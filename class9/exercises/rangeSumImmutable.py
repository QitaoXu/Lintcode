class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        
        self.prefix_sum = [0]
        
        prefix_sum = 0 
        
        for num in nums:
            
            prefix_sum += num 
            
            self.prefix_sum.append(prefix_sum)
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.prefix_sum[j + 1] - self.prefix_sum[i]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)