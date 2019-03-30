class Solution:
    """
    @param A: A an integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def totalOccurrence(self, A, target):
        # write your code here
        
        if not A or target == None:
            return 0 
            
        start, end = 0, len(A) - 1 
        
        nums = A
        
        while (start + 1) < end:
            
            mid = ( start + end ) // 2
            
            if nums[mid] < target:
                start = mid 
                
            if nums[mid] == target:
                end = mid 
                
            if nums[mid] > target:
                end = mid 
                
        
        if nums[start] == target:
            head = start
        elif nums[end] == target:
            head = end 
        else:
            head = -1 

        
        start, end = 0, len(A) - 1 
        
        while (start + 1) < end:
            
            mid = ( start + end ) // 2 
            
            if nums[mid] < target:
                start = mid 
                
            if nums[mid] == target:
                start =  mid 
                
            if nums[mid] > target:
                end = mid 
                
        if nums[end] == target:
            tail = end 
        elif nums[start] == target:
            tail = start
        else:
            tail = -1 
            
        if head >= 0 and tail >= 0:
            return tail - head + 1 
        else:
            return 0