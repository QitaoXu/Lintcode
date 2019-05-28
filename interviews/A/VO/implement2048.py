DIRECTION_TO_DELTA = {"left" : (-1, 0),
                      "right" : (1, 0),
                      "up" : (0, 1),
                      "down" : (0, -1)}
class Solution:

    def merge2048(self, grid, path):

        for point, direction in path:

            self.getNextState(grid, point, direction)

        return grid 

    def getNextState(self, grid, point, direction):

        x, y = point[0], point[1]
        dx, dy = DIRECTION_TO_DELTA[direction]

        nx, ny = x + dx, y + dy 

        if not self.isValid(grid, nx, ny):
            return 

        grid[nx][ny] += grid[x][y]

    def isValid(self, grid, x, y):

        m, n = len(grid), len(grid[0])

        if x < 0 or x >= m or y < 0 or y >= n:
            return False 

        return True 

