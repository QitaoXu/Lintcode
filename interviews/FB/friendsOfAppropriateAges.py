class Solution:
    """
    @param ages: 
    @return: nothing
    """
    def numFriendRequests(self, ages):
        # 
        
        if not ages:
            
            return 0 
        
        age_to_count = {} 
        
        for age in ages:
            
            age_to_count[age] = age_to_count.get(age, 0) + 1 
            
        res = 0 
            
        for a in age_to_count:
            
            for b in age_to_count:
                
                if self.request(a, b):
                    
                    res += age_to_count[a] * age_to_count[b] if a != b \
                            else age_to_count[a] * (age_to_count[b] - 1)
                    
        return res 
        
    def request(self, a, b):
        
        return not (b <= 0.5 * a + 7 or b > a or b > 100 and a < 100)
