from heapq import heappush, heappop
class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """
    def mergekSortedArrays(self, arrays):
        # write your code here
        
        # return self.mergekSortedArraysHelper(arrays, 0, len(arrays) - 1)
        return self.heap_method(arrays)
        # return self.merge2By2(arrays)
        
    def heap_method(self, arrays):
        
        if not arrays:
            return None 
            
        heap = [] 
        res = [] 
        
        for i in range(len(arrays)):
            
            if not arrays[i]:
                continue 
            
            heappush(heap, (arrays[i][0], 0, i))
            
        while heap:
            
            val, index, i = heappop(heap)
            
            res.append(val)
            
            index += 1 
            
            if index < len(arrays[i]):
                
                heappush(heap, (arrays[i][index], index, i))
                
        return res 
            
    def merge2By2(self, arrays):
        
        if not arrays:
            return None
            
        while len(arrays) > 1:
            
            new_arrays = [] 
            
            for i in range(0, len(arrays), 2):
                
                if i + 1 >= len(arrays):
                    break 
                
                new_array = self.mergeTwoArrays(arrays[i], arrays[i + 1])
                
                new_arrays.append(new_array)
                
            if len(arrays) % 2 == 1:
                new_arrays.append(arrays[-1])
                
            arrays = new_arrays
                
        return arrays[0]
            
        
    
    def mergekSortedArraysHelper(self, arrays, start, end):
        
        if start >= end:
            
            return arrays[start]
            
        mid = (start + end) // 2 
            
        left = self.mergekSortedArraysHelper(arrays, start, mid)
        right = self.mergekSortedArraysHelper(arrays, mid + 1, end)
        
        return self.mergeTwoArrays(left, right)
        
    def mergeTwoArrays(self, A, B):
        
        array_size = len(A) + len(B)
        
        array = [0 for _ in range(array_size)]
        
        
        left, right, index = 0, 0, 0 
        
        while left < len(A) and right < len(B):
            
            if A[left] < B[right]:
                
                array[index] = A[left]
                
                index += 1 
                left += 1 
                
            else:
                
                array[index] = B[right]
                index += 1 
                right += 1 
                
                
        while left < len(A):
            
            array[index] = A[left]
            index += 1 
            left += 1 
            
        while right < len(B):
            
            array[index] = B[right]
            index += 1 
            right += 1 
            
            
        return array 