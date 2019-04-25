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
            
        dq = deque([])
        
        for i in range(k - 1):
            self.push(dq, nums, i)
        
        result = []
        for i in range(k - 1, len(nums)):
            self.push(dq, nums, i)
            result.append(nums[dq[0]])
            if dq[0] == i - k + 1:
                dq.popleft()
                
        return result
            
    def push(self, dq, nums, i):
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        dq.append(i)