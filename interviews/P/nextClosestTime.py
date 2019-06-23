class Solution:
    def nextClosestTime(self, time):
        
        h, m = time.split(":")
        
        curr = int(h) * 60 + int(m)  
        
        result = None
        
        for i in range(curr + 1, curr + 1441):
            t = i % 1440 
            
            h, m = t // 60, t % 60 
            
            result = "%02d:%02d" % (h, m)
            
            if set(result) <= set(time): 
                break
                
        return result
            
            