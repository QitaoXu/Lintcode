class Solution:
    """
    @param nums: the given array
    @param k: the given number
    @return:  whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k
    """
    def containsNearbyDuplicate(self, nums, k):
        # Write your code here
        
        hash_set = set()
        
        for i in range(len(nums)):
            
            if nums[i] in hash_set:
                
                return True 
                
            hash_set.add(nums[i])
            
            if len(hash_set) > k:
                
                hash_set.remove(nums[i - k])
                
        return False 
        