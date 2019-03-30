class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    def sortColors(self, nums):
        # write your code here
        if nums == None or len(nums) == 0:
            return 
        
        left, index, right = 0, 0, len(nums) - 1 
        
        while index <= right:
            if nums[index] == 0:
                nums[left], nums[index] = nums[index], nums[left]
                left += 1 
                index += 1 
            
            elif nums[index] == 1:
                index += 1 
                
            else:
                nums[right], nums[index] = nums[index], nums[right]
                right -= 1 
                # index += 1 
        
        # A = nums
        # left, index, right = 0, 0, len(A) - 1

        # # be careful, index < right is not correct
        # while index <= right:
        #     if A[index] == 0:
        #         A[left], A[index] = A[index], A[left]
        #         left += 1
        #         index += 1
        #     elif A[index] == 1:
        #         index += 1
        #     else:
        #         A[right], A[index] = A[index], A[right]
        #         right -= 1