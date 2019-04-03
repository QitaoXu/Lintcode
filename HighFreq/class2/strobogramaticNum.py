class Solution:
    """
    @param num: a string
    @return: true if a number is strobogrammatic or false
    """
    def isStrobogrammatic(self, num):
        # write your code here
        
        mapping = { '0' : '0', '1' : '1', '6' : '9',
                    '8' : '8', '9' : '6' } 
                    
        start, end = 0, len(num) - 1 
        
        while start <= end:
            
            if num[start] not in mapping or mapping[num[start]] != num[end]:
                
                return False 
                
            start += 1 
            end -= 1 
            
        return True 
