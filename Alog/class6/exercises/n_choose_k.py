class Solution:
    """
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """
    def combine(self, n, k):
        # write your code here
        results, k_subset = [], []
        
        self.combine_helper(n, k, 1, k_subset, results)
        
        return results
    
    
    def combine_helper(self, n, k, start, k_subset, results):
        
        if len(k_subset) == k:
            results.append(k_subset.copy())
            return 
        
        for i in range(start, n + 1):
            
            k_subset.append(i)
            self.combine_helper(n, k, i + 1, k_subset, results)
            k_subset.pop()

solution = Solution()
n, k = 4, 2
print(solution.combine(n, k))

