class Solution:
    """
    @param str: A string
    @return: An integer
    """
    def atoi(self, str):
        # write your code here
        
        str = str.strip()
        
        if str == "" :
            
            return 0
            
        i = 0
        sign = 1
        num = 0
        length = len(str)
        MaxInt = (1 << 31) - 1
        
        if str[i] == '+':
            i += 1
            
        elif str[i] == '-' :
            i += 1
            sign = -1
        
        for i in range(i, length) :
            if str[i] < '0' or str[i] > '9' :
                break
            
            num = num * 10 + int(str[i])
            
            if num > MaxInt:
                break
            
        num *= sign
        
        if num >= MaxInt:
            return MaxInt
            
        if num < MaxInt * -1 :
            return MaxInt * - 1 - 1 
            
        return num
        
       