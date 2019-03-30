class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        # write your code here
        
        if not A:
            return 1 
            
        nums = A
        
        start, end = 1, len(nums) - 2
        
        while ( start + 1 ) < end:
            
            mid = ( start + end ) // 2  
            
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid 
                
            elif nums[mid - 1] < nums[mid] < nums[mid + 1]:
                start = mid  
                
            elif nums[mid -1 ] > nums[mid] >nums[mid + 1]:
                end = mid
                
            elif nums[mid] < nums[mid - 1] and nums[mid] < nums[mid + 1]:
                end = mid
        
        if nums[start] > nums[end]:
            return start
        else:
            return end