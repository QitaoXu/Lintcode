class Solution:
    def strStr2(self, source, target):
        
        if source is None or target is None:
            return -1 
            
        if len(target) == 0:
            return 0 
            
        if source[0 : len(target)] == target:
            return 0
            
        BASE = 1000000 
        
        m = len(target)
        
        targetCode = 0 
        
        for i in range(0, len(target)):
            
            targetCode = ( targetCode * 31 + ord(target[i]) ) % BASE 
            
        power = 1 
        
        for i in range(0, len(target)):
            
            power = ( power * 31 ) % BASE 
            
        hashCode  = 0 
        
        for i in range(len(source)):
            
            hashCode = ( hashCode * 31 + ord(source[i]) ) % BASE 
            
            if i < m:
                continue 
            
            if i >= m:
                
                hashCode = (hashCode - power * ord(source[i - m])) % BASE 
                
                if hashCode < 0:
                    hashCode += BASE 
                    
                if hashCode == targetCode:
                    
                    if source[i - m + 1: i + 1] == target:
                        return i - m  + 1 
                        
        return -1
                
        
        
        
        

                    
                    
                    
            
            
