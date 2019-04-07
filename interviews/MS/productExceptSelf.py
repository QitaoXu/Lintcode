class Solution:
    """
    @param nums: an array of integers
    @return: the product of all the elements of nums except nums[i].
    """
    def productExceptSelf(self, nums):
        # write your code here
        
        product = [1 for _ in range(len(nums))]
        
        prefix_product = 1 
        
        for i in range(1, len(nums)):
            
            prefix_product *= nums[i - 1]
            
            product[i] *= prefix_product
            
        suffix_product = 1 
        
        for j in range(len(nums) - 2, -1, -1):
            
            suffix_product *= nums[j + 1]
            
            product[j] *= suffix_product
            
        return product