class Solution:
    """
    @param arr: The prime array
    @return: Return the array of all of prime product
    """
    def getPrimeProduct(self, arr):
        # Write your code here
        
        results = [] 
        
        self.dfs(arr, [], 0, 1, results)
        
        results.sort()
        
        return results 
        
    def dfs(self, arr, combination, start_index, product, results):
        
        if len(combination) > 1: 
            
            results.append(product)
            
        
        for i in range(start_index, len(arr)):
            
            combination.append(arr[i])
            
            self.dfs(arr, combination, i + 1, product * arr[i], results)
            
            combination.pop()