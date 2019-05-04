from collections import deque    
    
class Solution:
    """
    @param nums: A list of integers.
    @param k: An integer
    @return: The maximum number inside the window at each moving.
    """
    def maxSlidingWindow(self, nums, k):
        # write your code here
        
        if not nums or not k:
            return []
        
        dq = deque()
        
        results = [] 
        
        for i in range(0, k):
            self.push(dq, nums, i)
        results.append(nums[dq[0]])
            
        for i in range(k, len(nums)):
            
            self.push(dq, nums, i)
            
            if dq[0] == i - k:
                dq.popleft()
            
            results.append(nums[dq[0]])
            
                
        return results 
        
    def push(self, dq, nums, i):
        
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
            
        dq.append(i)