import sys 

class Garden:

    def canArrange(self, board, s, h): 

        m = len(board)
        n = len(board[0])

        row = [0 for _ in range(m)]
        col = [0 for _ in range(n)] 
        flowers = 0

        for i in range(m):
            for j in range(n): 
                if board[i][j] == "*":
                    row[i] += 1
                    col[j] += 1 
                    flowers += 1

        rowCap = flowers // (s + 1) 
        rowPart = 0 
        rowCount = s + 1
        rowArrange = False 

        for num in row: 

            rowPart += num  

            if rowPart < rowCap: 
                continue 
            elif rowPart == rowCap:
                rowPart = 0
                rowCount -= 1 

            else:
                break 

        if rowPart == 0 and rowCount == 0:
            rowArrange = True 

        else: 
            rowArrange = False 

        colCap = flowers // (h + 1) 
        colCount = h + 1
        colPart = 0
        colArrange = False 

        for num in col:

            colPart += num 

            if colPart < colCap:
                continue 
            elif colPart == colCap:
                colPart = 0
                colCount -= 1 

            else:
                break 

        if colPart == 0 and colCount == 0:
            colArrange = True 
        else:
            colArrange = False 

        return rowArrange and colArrange


garden = Garden() 
board = []
for line in sys.stdin: 

    line = line.rstrip()
    if line == "done":
        break
    board.append(line.split())

s = 0
h = 0 

print("Please input s")
for line in sys.stdin:
    
    line = line.rstrip()
    s = int(line)
    break 

print("Please input h")
for line in sys.stdin:
    
    line = line.rstrip()
    h = int(line)
    break 

print(garden.canArrange(board, 1, 1)) 




