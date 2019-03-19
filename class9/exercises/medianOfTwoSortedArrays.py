class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        # write your code here
        
        n = len(A) + len(B)
        
        if n % 2 == 1:
            
            return self.find_kth(A, B, 0, 0, n // 2 + 1) / 1.0
            
        else:
            
            return (self.find_kth(A, B, 0, 0, n // 2) + \
                    self.find_kth(A, B, 0, 0, n // 2 + 1)) / 2
        
    def find_kth(self, A, B, A_start, B_start, k):
        
        if A_start >= len(A):
            return B[B_start + k - 1]
            
        if B_start >= len(B):
            return A[A_start + k - 1]
            
        if k == 1:
            return min(A[A_start], B[B_start])
            
        A_key = A[A_start + k // 2 - 1] if A_start + k // 2 - 1 < len(A) else sys.maxsize
        B_key = B[B_start + k // 2 - 1] if B_start + k // 2 - 1 < len(B) else sys.maxsize 
        
        if A_key < B_key:
            
            return self.find_kth(A, B, A_start + k // 2, B_start, k - k // 2)
            
        else:
            
            return self.find_kth(A, B, A_start, B_start + k // 2, k - k // 2)