class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        
        hashSet = {}
        
        for i in range(len(numbers)):
            
            if target - numbers[i] in hashSet.keys():
                return [ hashSet[target - numbers[i]], i]
                
            hashSet[numbers[i]] = i  
        
        return None