class Solution:
    """
    @param logs: the logs
    @return: the log after sorting
    """
    def logSort(self, logs):
        # Write your code here
        if not logs:
            return []
        
        letter_logs = [] 
        digit_logs = [] 
        
        for log in logs:
            
            index = log.find(" ")
            
            if log[index + 1].isdigit():
                digit_logs.append(log)
                
            else:
                
                log_id = log[:index]
                log_content = log[index + 1:]
                
                letter_logs.append((log, log_content, log_id))
                
        letter_logs = sorted(letter_logs, key = lambda letter_log : (letter_log[1], letter_log[2]))
        
        l_logs = [] 
        
        for letter_log in letter_logs:
            l_logs.append(letter_log[0])
            
        return l_logs + digit_logs