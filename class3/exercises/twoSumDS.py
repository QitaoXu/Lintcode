class TwoSum:
    """
    @param number: An integer
    @return: nothing
    """
    def __init__(self):
        self.count = {}
        
    def add(self, number):
        # write your code here
        if number in self.count.keys():
            self.count[number] += 1 
        else:
            self.count[number] = 1 
        

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # write your code here
        for num in self.count.keys():
            if value - num in self.count.keys() and (value - num != num or self.count[num] > 1):
                return True 
                
        return False 