class Solution:
    """
    @param n: a integer
    @param logs: a list of integers
    @return: return a list of integers
    """
    def exclusiveTime(self, n, logs):
        # write your code here
        
        points = [] 
        
        result = [0 for _ in range(n)]
        
        for log in logs:
            
            sub_log = log.split(':')
            
            function_id, is_start, timestamp = sub_log[0], sub_log[1], sub_log[2]
            
            function_id = int(function_id)
            is_start = True if is_start == "start" else False 
            timestamp = int(timestamp) if is_start else int(timestamp) + 1 
            
            points.append((timestamp, function_id, is_start))
        
        stack = [] 
        
        last_timestamp = 0 
        
        for timestamp, function_id, is_start in points:
            
            if is_start:
                
                if stack:
                    
                    result[stack[-1]] += timestamp - last_timestamp
                
                stack.append(function_id)
                
            else:
                
                result[stack.pop()] += timestamp - last_timestamp
                
            last_timestamp = timestamp
        
        return result