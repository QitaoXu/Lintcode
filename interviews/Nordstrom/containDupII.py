class Solution:
    def containsNearbyDuplicate(self, nums, k):
        
        hash_set = set()
        
        for i in range(len(nums)):
            
            if nums[i] in hash_set:
                
                return True 
            
            hash_set.add(nums[i])
            
            if len(hash_set) > k:
                
                hash_set.remove(nums[i - k])
            
        return False 