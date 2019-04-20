class Solution:
    """
    https://leetcode.com/problems/super-washing-machines/discuss/235584/Explanation-of-Java-O(n)-solution
    @param machines: an integer array representing the number of dresses 
        in each washing machine from left to right on the line
        
    @return: the minimum number of moves to make all the washing machines 
        have the same number of dresses
    """
    def findMinMoves(self, machines):
        # Write your code here
        
        total = 0 
        
        for clothes in machines:
            total += clothes
            
        if total % len(machines) != 0:
            
            return -1 
            
        avg = total // len(machines)
        
        maxOffload = 0 
        maxRunningBlance = 0 
        
        runningBalance = 0 
        
        for clothes in machines:
            
            offload = clothes - avg 
            
            runningBalance += offload 
            
            maxRunningBlance = max(maxRunningBlance, abs(runningBalance))
            maxOffload = max(maxOffload, offload)
            
        return max(maxOffload, maxRunningBlance)
            