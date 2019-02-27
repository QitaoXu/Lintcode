class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):

        if matrix == [] or matrix == [[]]:
            return False

        row, col = len(matrix), len(matrix[0])

        start, end = 0, row * col - 1 

        while ( start + 1 ) < end:

            mid = ( start + end ) // 2 

            x, y = mid // col, mid % col 

            if matrix[x][y] < target:
                start = mid 

            elif matrix[x][y] == target:
                return True 

            elif matrix[x][y] > target:
                end = mid 

        x, y = start // col, start % col 

        if matrix[x][y] == target:
            return True 

        x, y = end // col, end % col

        if matrix[x][y] == target:
            return True 

        return False
