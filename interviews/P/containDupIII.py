class Solution:
    """
    @param nums: the given array
    @param k: the given k
    @param t: the given t
    @return: whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.
    """
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        # Write your code here
        
        hash_set = set()
        
        for i in range(len(nums)):
            
            for diff in range(0, t + 1):
                
                if nums[i] - diff in hash_set or nums[i] + diff in hash_set:
                    
                    return True 
                    
            hash_set.add(nums[i])
            
            if len(hash_set) > k:
                
                hash_set.remove(nums[i - k])
                
        return False 