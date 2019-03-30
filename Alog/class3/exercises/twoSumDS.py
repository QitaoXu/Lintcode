class TwoSum:
    """
    @param number: An integer
    @return: nothing
    """
    def __init__(self):
        self.num_to_count = {}
        
    def add(self, number):
        # write your code here
        
        if number in self.num_to_count:
            
            self.num_to_count[number] += 1 
            
        else:
            
            self.num_to_count[number] = 1 
        
        

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # write your code here
        
        for num in self.num_to_count:
            
            if value - num in self.num_to_count and (value - num != num or self.num_to_count[num] > 1):
                
                return True 
                
        return False 