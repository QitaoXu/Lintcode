class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        # write your code here
        
        candidates.sort()
        selected = [] 
        results = [] 
        
        self.comSumHelper(candidates, selected, 0, results, target)
        
        return results 

    def comSumHelper(self, candidates, selected, start_index, results, target):
        
        if target == 0:
            results.append(selected.copy())
            return 
        
        for i in range(start_index, len(candidates)):
            
            if target < candidates[i]:
                return
            
            if i != 0 and candidates[i] == candidates[i - 1] and i > start_index:
                continue 
            
            selected.append(candidates[i])
            self.comSumHelper(candidates, selected, i, results, target - candidates[i])
            selected.pop()