class Solution:

    def getViceDiagMatrix(self, matrix):

        if not matrix or len(matrix) != len(matrix[0]):
            return [] 
        
        n = len(matrix)

        res = [[] for _ in range((n - 1) * 2 + 1 )]

        # 1 -> 1, 2 -> 3, 3 -> 5 

        for i in range(n):
            for j in range(n):

                index = i + j 
                res[index].append(matrix[i][j])

        return res 

solution = Solution()

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

print(solution.getViceDiagMatrix(matrix))

