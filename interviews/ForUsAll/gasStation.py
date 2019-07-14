class Solution:
    def canCompleteCircuit(self, gas, cost):
        
        curt_tank, total_tank = 0, 0 
        starting_pos = 0 
        
        for i in range(0, len(gas)):
            
            curt_tank += gas[i] - cost[i]
            total_tank += gas[i] - cost[i]
            
            if curt_tank < 0:
                
                starting_pos = i + 1 
                curt_tank = 0 
                
        return starting_pos if total_tank >= 0 else -1 