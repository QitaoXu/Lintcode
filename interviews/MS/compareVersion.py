class Solution:
    """
    @param version1: the first given number
    @param version2: the second given number
    @return: the result of comparing
    """
    def compareVersion(self, version1, version2):
        # Write your code here
        
        v1_list = version1.split('.')
        v2_list = version2.split('.')
        
        for i in range( max(len(v1_list), len(v2_list)) ):
            
            v1 = int(v1_list[i]) if i < len(v1_list) else 0 
            v2 = int(v2_list[i]) if i < len(v2_list) else 0 
            
            if v1 > v2:
                
                return 1 
                
            elif v1 < v2:
                
                return -1 
                
            else:
                
                continue 
            
        return 0
    def version_to_num(self, version):
        
        int_part = []
        dec_part = [] 

        dot = False 
        
        for c in version:
            
            if not dot: # integer part
                
                if c == '0':
                    
                    continue 
                
                elif c == '.':
                    
                    dot = True 
                    
                else:
                    
                    int_part.append(c)
            
            else: # decimal part 
                
                dec_part.append(c)
                
        num = 0
        
        for digit in int_part:
            
            num = num * 10 + int(digit)
            
        for i in range(len(dec_part)):
            
            num += float(dec_part[i]) * (1 / (10 ** (i + 1)))
            
        return num 