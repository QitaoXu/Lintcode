from heapq import heappush, heappop

class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums, k):
        # write your code here
        
        # Solution 2: Quick Select
        
        self.quick_select(nums, 0, len(nums) - 1, k)
        
        results = nums[:k]
        
        results.sort(reverse = True)
        
        return results
    
        
    def quick_select(self, nums, start, end, k):
        
        if start >= end:
            
            return 
        
        left, right = start, end 
        
        pivot = nums[(start + end) // 2]
        
        while left <= right:
            
            while left <= right and nums[left] > pivot:
                
                left += 1 
                
            while left <= right and nums[right] < pivot:
                
                right -= 1 
                
            if left <= right:
                
                nums[left], nums[right] = nums[right], nums[left]
                
                left += 1 
                right -= 1 
                
                
        if start + k - 1 <= right:
            
            self.quick_select(nums, start, right, k)
            
        if start + k - 1 >= left:
            
            self.quick_select(nums, left, end, k - (left - start))
            
        return 
    
    # def topk(self, nums, k):
    
        # Solution 1: Heap
        # heap = [] 
        
        # for num in nums:
            
        #     heappush(heap, num)
            
        #     if len(heap) > k:
                
        #         heappop(heap)
        
        # results = []
            
        # while heap:
            
        #     results.append(heappop(heap))
            
        # results.reverse()
        
        # return results 