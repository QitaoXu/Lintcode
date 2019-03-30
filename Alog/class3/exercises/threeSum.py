class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        results = []
        nums = numbers
        if nums == None or len(nums) < 3:
            return results
            
         
        # nums.sort() 
        # self.quickSort(nums, 0, len(nums) - 1)
        
        temp = [0] * len(nums)
        self.mergeSort(nums, 0, len(nums) - 1, temp)
        
        length = len(nums)
        
        for i in range(0, length - 2):
            if i and nums[i] == nums[i - 1]:
                continue 
            
            left, right = i + 1, length - 1 
            target = -nums[i]
            
            while left < right:
                
                if nums[left] + nums[right] == target:
                    results.append(  [nums[i], nums[left], nums[right]]  )
                    left += 1 
                    right -= 1 
                    
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1 
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1 
                    
                elif nums[left] + nums[right] < target:
                    left += 1 
                    
                else:
                    right -= 1 
                    
                    
        return  results 
            
    
    def quickSort(self, nums, start, end):
        
        if start >= end:
            return 
        
        left, right = start, end 
        
        pivot = nums[(start + end) // 2] 
        
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
        
        mid = (start + end) // 2 
        
        self.mergeSort(nums, start, mid, temp)
        self.mergeSort(nums, mid + 1, end, temp)
        self.merge(nums, start, end, temp)
        
    
    def merge(self, nums, start, end, temp):
        
        mid = (start + end) // 2 
        leftIndex, rightIndex = start, mid + 1 
        index = leftIndex
        
        while leftIndex <= mid and rightIndex <= end:
            
            if nums[leftIndex] <= nums[rightIndex]:
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
            
            
        
            
            
            
            
            
            
            