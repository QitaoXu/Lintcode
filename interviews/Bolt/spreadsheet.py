class Spreadsheet:

    def __init__(self):

        self.sheet = [[None for _ in range(26)] for _ in range(26)] 

    def _set(self, cell, value): 
        # pass 

        row, col = cell[0], cell[1:]  

        row_num, col_num = self.get_row_num(row), self.get_col_num(col) 

        self.sheet[row_num][col_num] = value 

    def query(self, cell):

        row, col = cell[0], cell[1:]  

        row_num, col_num = self.get_row_num(row), self.get_col_num(col) 

        return self.sheet[row_num][col_num]

    def eval(self, target_cell, expression):

        pass 

    def parse_expression(self, expression):

        n = len(expression)

        op = set(['+', '-', '*', '/']) 

        tokens = [] 

        last = 0 

        for i in range(n):

            if expression[i] in op:

                cell = expression[last : i] 

                tokens.append(self.query(cell)) 

                tokens.append(expression[i]) 

                last = i + 1 

        return tokens 

    def get_row_num(self, row):

        return ord(row) - ord('A')  

    def get_col_num(self, col):
        
        return int(col) - 1 
