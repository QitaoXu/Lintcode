class Solution:
    """
    @param tasks: the given char array representing tasks CPU need to do
    @param n: the non-negative cooling interval
    @return: the least number of intervals the CPU will take to finish all the given tasks
    """
    def leastInterval(self, tasks, n):
        # write your code here
        
        task_to_times = {} 
        
        for task in tasks:
            
            if task not in task_to_times:
                
                task_to_times[task] = 0
                
            task_to_times[task] += 1 
            
        longest = max(task_to_times.values())
        
        ans = (longest - 1) * (n + 1)
        
        for times in task_to_times.values():
            
            if times == longest:
                
                ans += 1 
                
        return max(len(tasks), ans)