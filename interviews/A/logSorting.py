class Solution:
    """
    @param logs: the logs
    @return: the log after sorting
    """
    def logSort(self, logs):
        # Write your code here
        
        type1, type2 = [], [] 
        
        for log in logs:
            
            index = log.find(" ")
            
            if log[index + 1].isdigit():
                
                type2.append(log)
                
            else:
                
                log_id = log[:index]
                log_content = log[index + 1:]
                
                type1.append((log, log_content, log_id))
                
        type1 = sorted(type1, key = lambda t1 : (t1[1], t1[2]))
        
        output = [] 
        
        for t1 in type1:
            
            output.append(t1[0])
            
        return output + type2 