class Solution:
    """
    @param p: the point List
    @return: the numbers of pairs which meet the requirements
    """
    def pairNumbers(self, p):
        # Write your code here
        
        if len(p) < 2:
            
            return 0
        
        odd_odd, odd_even, even_even, even_odd = 0, 0, 0, 0 
        
        points = p 
        
        for point in points:
            
            if point.x % 2 == 1:
                
                if point.y % 2 == 1:
                    
                    odd_odd += 1 
                    
                else:
                    
                    odd_even += 1 
                    
            else:
                
                if point.y % 2 == 1:
                    
                    even_odd += 1 
                    
                else:
                    
                    even_even += 1 
                    
        count = 0 
        
        count += odd_odd * (odd_odd - 1) // 2 
        
        count += odd_even * (odd_even - 1) // 2 
        
        count += even_odd * (even_odd - 1) // 2 
        
        count += even_even * (even_even - 1) // 2 
        
        return count 