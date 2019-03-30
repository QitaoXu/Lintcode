ONE = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
TEN = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
HUNDRED = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
THOUSAND = ['', 'M', 'MM', 'MMM']

TABLE = [ONE, TEN, HUNDRED, THOUSAND]

class Solution:
    """
    @param n: The integer
    @return: Roman representation
    """
    def intToRoman(self, n):
        # write your code here
        
        if n <= 0 or n > 4000:
            
            return ''
            
        result = [] 
        
        divide_count = 0
        
        while n > 0:
            
            end_digit = n % 10 
            
            result.append(TABLE[divide_count][end_digit])
            
            n = n // 10 
            
            divide_count += 1 
            
        result.reverse()
        
        return ''.join(result)