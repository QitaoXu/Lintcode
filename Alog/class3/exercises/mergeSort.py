class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers2(self, A):
        # write your code here
        
        if A == None and len(A) == 0:
            return 
        
        temp = [0] * len(A)
        self.mergeSort(A, 0, len(A) - 1, temp)
        
    def mergeSort(self, nums, start, end, temp):
        
        if start >= end:
            return 
        
        self.mergeSort(nums, start, (start + end) // 2, temp)
        self.mergeSort(nums, (start + end) // 2 + 1, end, temp)
        self.merge(nums, start, end, temp)
        
    def merge(self, nums, start, end, temp):
        
        mid = ( start + end ) // 2 
        
        leftIndex = start 
        rightIndex = mid + 1 
        
        index = leftIndex 
        
        while leftIndex <= mid and rightIndex <= end:
            
            if nums[leftIndex] < nums[rightIndex]:
                temp[index] = nums[leftIndex]
                index += 1 
                leftIndex += 1 
                
            else:
                temp[index] = nums[rightIndex]
                index += 1 
                rightIndex += 1 
                
        while leftIndex <= mid:
            temp[index] = nums[leftIndex]
            index += 1 
            leftIndex += 1 
            
        while rightIndex <= end:
            temp[index] = nums[rightIndex]
            index += 1 
            rightIndex += 1 
        
        for i in range(start, end + 1):
            nums[i] = temp[i]
            