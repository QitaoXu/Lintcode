class Solution:
    """
    @param board: the given board
    @return: True if and only if it is possible to reach this board position during the course of a valid tic-tac-toe game
    """
    def validTicTacToe(self, board):
        # Write your code 
        
        num_X, num_O = 0, 0 
        
        for i in range(3):
            for j in range(3):
                
                if board[i][j] == 'X':
                    num_X += 1 
                    
                elif board[i][j] == 'O':
                    num_O += 1 
                    
        if not (num_X == num_O or num_X == num_O + 1):
            return False 
            
        for i in range(3):
            
            if board[i][0] == board[i][1] == board[i][2]:
                
                if board[i][0] == 'X':
                    return num_X == num_O + 1 
                    
                if board[i][0] == 'O':
                    return num_X == num_O 
                    
        for j in range(3):
            
            if board[0][j] == board[1][j] == board[2][j]:
                
                if board[0][j] == 'X':
                    return num_X == num_O + 1 
                    
                if board[0][j] == 'O':
                    return num_X == num_O 
                    
        
        if board[0][0] == board[1][1] == board[2][2]:
            
            if board[0][0] == 'X':
                return num_X == num_O + 1 
                
            if board[0][0] == 'O':
                return num_X == num_O 
                
        if board[0][2] == board[1][1] == board[2][0]:
            if board[0][2] == 'X':
                return num_X == num_O + 1 
                
            if board[0][2] == 'O':
                return num_X == num_O 
                
        return True 