class Solution:
    """
    @param num: a string contains only digits 0-9
    @param target: An integer
    @return: return all possibilities
    """
    def addOperators(self, num, target):
        # write your code here
        
        start_index = 0 
        
        curt_exp = ""
        
        sum_up = 0
        
        last_factor = 0 
        
        results = [] 
        
        self.dfs(num, target, start_index, curt_exp, sum_up, last_factor, results)
        
        return results 
        
    def dfs(self, num, target, start_index, curt_exp, sum_up, last_factor, results):
        
        if start_index == len(num):
            
            if sum_up == target:
                
                results.append(curt_exp)
                
            return 
        
        for i in range(start_index + 1, len(num) + 1):
            
            prefix_num = int(num[start_index: i])
            
            if start_index == 0:
                
                self.dfs(num, target, i, "" + str(prefix_num), prefix_num, prefix_num, results)
                
            else:
                
                self.dfs(num, target, i, curt_exp + "+" + str(prefix_num), sum_up + prefix_num, prefix_num, results)
                self.dfs(num, target, i, curt_exp + "-" + str(prefix_num), sum_up - prefix_num, -prefix_num, results)
                self.dfs(num, target, i, curt_exp + "*" + str(prefix_num), sum_up - last_factor + last_factor * prefix_num, last_factor * prefix_num, results)
                
                
            if prefix_num == 0:# e.g. "06" cannot be regarded as a valid number
                
                break 