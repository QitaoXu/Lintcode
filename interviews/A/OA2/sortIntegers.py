class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers2(self, A):
        # write your code here
        if not A:
            return 
        
        # self.quickSort(A, 0, len(A) - 1)
        
        temp = [0 for _ in range(len(A))]
        
        self.mergeSort(A, 0, len(A) - 1, temp)
        
    def quickSort(self, nums, start, end):
        
        if start >= end:
            return 
        
        left = start
        right = end 
        
        pivot = nums[left + (right - left) // 2]
        
        while left <= right:
            
            while left <= right and nums[left] < pivot:
                
                left += 1 
                
            while left <= right and nums[right] > pivot:
                
                right -= 1 
                
            if left <= right:
                
                nums[left], nums[right] = nums[right], nums[left]
                left += 1 
                right -= 1 
                
        self.quickSort(nums, start, right)
        self.quickSort(nums, left, end)
        
    def mergeSort(self, nums, start, end, temp):
        if start >= end:
            return 
        
        mid = start + (end - start) // 2 
        self.mergeSort(nums, start, mid, temp)
        self.mergeSort(nums, mid + 1, end, temp)
        
        self.merge(nums, start, end, temp)
        
    def merge(self, nums, start, end, temp):
        
        mid = start + (end - start) // 2 
        left, right = start, mid + 1 
        index = start
        
        while left <= mid and right <= end:
            
            if nums[left] < nums[right]:
                temp[index] = nums[left]
                index += 1 
                left += 1 
                
            else:
                temp[index] = nums[right]
                index += 1 
                right += 1 
                
        while left <= mid:
            temp[index] = nums[left]
            index += 1 
            left += 1 
            
        while right <= end:
            temp[index] = nums[right]
            index += 1 
            right += 1 
            
        for i in range(start, end + 1):
            nums[i] = temp[i]
                
                
            
        
                
        
