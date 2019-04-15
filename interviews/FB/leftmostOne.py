class Solution:
    """
    @param arr: The 2-dimension array
    @return: Return the column the leftmost one is located
    """
    def getColumn(self, arr):
        # Write your code here
        
        idx = len(arr[0]) - 1
        
        for i in range(len(arr)):
            
            while idx >= 0:
                
                if arr[i][idx] == 0:
                    
                    break 
                
                idx -= 1 
                
        return idx + 1 
