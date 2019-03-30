class Solution:
    """
    @param num: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, num, target):
        # write your code here
        
        results = [] 
        combination = [] 
        
        num.sort()
        
        self.comSumhelper(num, combination, 0, results, target)
        
        return results
        
        
    def comSumhelper(self, num, combination, start_index, results, target):
        
        if target == 0:
            results.append(combination.copy())
            return 
        
        for i in range(start_index, len(num)):
            
            if target < num[i]:
                return 
            
            if i != 0 and num[i] == num[i - 1] and i > start_index:
                continue 
            
            combination.append(num[i])
            self.comSumhelper(num, combination, i + 1, results, target - num[i])
            combination.pop()