class Solution:
    """
    @param stringIn: The original string.
    @param K: The length of substrings.
    @return: return the count of substring of length K and exactly K distinct characters.
    """
    def KSubstring(self, stringIn, K):
        # Write your code here
        if not stringIn or (K - 1) > len(stringIn):
            return 0 
        
        letter_to_count = {} 
        string = stringIn
        found = set()
        k = K 
        
        for i in range(k):
            
            letter_to_count[string[i]] = letter_to_count.get(string[i], 0) + 1 
            
        if len(letter_to_count) == k - 1:
            found.add(string[: k])
            
        for start in range(1, len(string) - k + 1):
            
            end = start +  k - 1 
            
            letter_to_count[string[end]] = letter_to_count.get(string[end], 0) + 1 
            letter_to_count[string[start - 1]] -= 1 
            
            if letter_to_count[string[start - 1]] == 0:
                del letter_to_count[string[start - 1]]
                
            if len(letter_to_count) == k - 1:
                found.add(string[start : end + 1])
                
        return len(found), sorted(list(found)) 

solution = Solution()
string = "abacdckf"
k = 4
print(solution.KSubstring(string, k))