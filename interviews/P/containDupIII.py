class Solution:
    """
    @param nums: the given array
    @param k: the given k
    @param t: the given t
    @return: whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.
    """
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        
        if t < 0:
            
            return False 
        
        bucket_to_num = {}
        
        w = t + 1 
        
        for i in range(len(nums)):
            
            m = self.get_ID(nums[i], w)
            
            if m in bucket_to_num:
                
                return True 
            
            if (m + 1) in bucket_to_num and abs(bucket_to_num[m + 1] - nums[i]) < w:
                return True  
            
            if (m - 1) in bucket_to_num and abs(bucket_to_num[m - 1] - nums[i]) < w:
                return True 
            
            bucket_to_num[m] = nums[i]
            
            if i >= k:
                del bucket_to_num[self.get_ID(nums[i - k], w)]
                
        return False 
        
    def get_ID(self, x, w):
        
        return  x // w
        # java 
        # return x < 0 ? (x + 1) / w - 1 : x / w