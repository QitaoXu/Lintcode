class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        # write your code here
        array_size = len(A) + len(B)
        
        array = [0 for _ in range(array_size) ]
        
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