class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """
    def mergekSortedArrays(self, arrays):
        # write your code here
        
        return self.mergekSortedArraysHelper(arrays, 0, len(arrays) - 1)
    
    
    def mergekSortedArraysHelper(self, arrays, start, end):
        
        if start >= end:
            return arrays[start]
        
        left = self.mergekSortedArraysHelper(arrays, start, (start + end) // 2)
        right = self.mergekSortedArraysHelper(arrays, (start + end) // 2 + 1, end)
        
        return self.mergeTwoArrays(left, right)
        
    def mergeTwoArrays(self, array1, array2):
        
        result = [0 for _ in range(len(array1) + len(array2))]
        
        left = 0
        
        right = 0 
        
        index = 0 
        
        while left < len(array1) and right < len(array2):
            
            if array1[left] < array2[right]:
                
                result[index] = array1[left]
                left += 1 
                index += 1 
                
            else:
                
                result[index] = array2[right]
                right += 1 
                index += 1 
                
        while left < len(array1):
            
            result[index] = array1[left]
            left += 1 
            index += 1 
            
        while right < len(array2):
            
            result[index] = array2[right]
            right += 1 
            index += 1 
            
        return result