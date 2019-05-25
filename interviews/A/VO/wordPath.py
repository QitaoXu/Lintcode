class Solution:

    def findWordPath(self, word, n):

        paths = [] 

        word = 'A' + word

        for i in range(0, len(word) - 1):

            path = self.getPath(word[i], word[i + 1], n)

            paths.append(path)

        return paths 

    def getPath(self, start, end, n):

        start_order = ord(start) - ord('A')
        start_row, start_col = start_order // n, start_order % n 

        end_order = ord(end) - ord('A')
        end_row, end_col = end_order // n, end_order % n  

        delta_row, delta_col = end_row - start_row, end_col - start_col 

        path = ""

        if delta_col > 0:

            for _ in range(delta_col):
                path += 'E'

        elif delta_col < 0:

            for _ in range(abs(delta_col)):
                path += 'W'

        if delta_row > 0:
            for _ in range(delta_row):
                path += 'S'

        elif delta_row < 0:
            for _ in range(abs(delta_row)):
                path += 'N'

        return path 


word = "HELLO"

n = 5 

solution = Solution()

print(solution.findWordPath(word, n))

        

