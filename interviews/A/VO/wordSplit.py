class Solution:

    def wordSplit(self, string, wordDict):

        results = [] 

        if not string:
            return results

        combination = []
        start_index = 0 

        self.dfs(string, start_index, combination, wordDict, results)
        
        return results

    def dfs(self, string, start_index, combination, wordDict, results):

        if start_index == len(string):

            results.append(combination[:])

            return 

        for i in range(start_index, len(string) + 1):
            prefix = string[start_index : i] 

            if prefix not in wordDict:
                continue 
            
            combination.append(prefix)

            self.dfs(string, i, combination, wordDict, results)

            combination.pop()


class MemoSolution:

    def wordSplit(self, string, wordDict):

        results = [] 

        if not string:
            return results

        combination = []
        # start_index = 0 
        memo = {}

        return self.dfs(string, combination, wordDict, results, memo)
         

    def dfs(self, string, combination, wordDict, results, memo):

        if string in memo:
            return memo[string]

        if len(string) == 0:

            return []

        partitions = [] 

        for i in range(1, len(string) + 1):
            prefix = string[ : i] 

            if prefix not in wordDict:
                continue 
            
            combination.append(prefix)

            sub_partitions = self.dfs(string[i : ], combination, wordDict, results, memo)

            for sub_partition in sub_partitions:
                partitions.append([prefix] + sub_partition)

            combination.pop() 

        if string in wordDict:
            partitions.append([string])

        memo[string] = partitions

        return memo[string]



solution = Solution()

string = "applepenapple"
wordDict = (["apple","pen","applepen"])

print(solution.wordSplit(string, wordDict))

memoSolution = MemoSolution()
print(memoSolution.wordSplit(string, wordDict))