# Classsic Binary Search

class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def findPosition(self, nums, target):

        if not nums:
            return -1 

        return self.binarySearch( nums, 0, len(nums) - 1, target )

    def binarySearch( self, nums, start, end, target ):

        if ( start > end ):
            return -1 

        mid = ( start + end ) // 2 # floor divide 

        if nums[mid] == target:
            return mid 

        if nums[mid] < target:
            return self.binarySearch( nums, mid + 1, end, target )

        return self.binarySearch( nums, start, mid - 1, target )