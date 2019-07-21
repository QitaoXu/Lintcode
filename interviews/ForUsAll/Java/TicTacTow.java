public class TicTacToe {

    private char[][] board;
    private int currentPlayer; 
    private char currentPlayerMark;
    private boolean gameEnd; 
    private int n; 

    public TicTacToe(int n) {
        this.board = new int[n][n]; 
        this.currentPlayer = 1;
        this.currentPlayerMark = 'X';
        this.gameEnd = false; 
        this.n = n; 

        for (int i = 0; i < n; i++) {
            for (int j = 0; i < n; j++) {
                this.board[i][j] = ' ';
            }
        }
    }

    public int move(int row, int col, int player) throws AlreadyTakenException, BoardFullException, GameEndException{


        if (this.gameEnd) {

            throw new GameEndException();
        }
        
        if (this.board[row][col] != ' ') {

            throw new AlreadyTakenException();
        }

        if (this.isBoardFull()) {

            throw new BoardFullException();
        }

        if (this.currentPlayer != player) {
            this.changePlayer();
        }

        this.board[row][col] = this.currentPlayerMark;

        if (this.isWin(row, col)) {
            this.gameEnd = true;
            return this.currentPlayer;
        }

        this.changePlayer();
        return 0;

    }

    private void changePlayer(){

        if (currentPlayer == 1) {
            currentPlayer = 2;
            currentPlayerMark = 'O'; 
        }
        else {
            currentPlayer = 1;
            currentPlayerMark = 'X';
        }
    }

    private boolean isBoardFull() {

        boolean isFull = false;

        for (int i = 0; i < this.n; i++) {

            for (int j = 0; j < this.n; j++) {

                if (this.board[i][j] == ' ') return false;
            }
        }

        this.gameEnd = true;
        return true;
    }

    private boolean isWin(int row, int col) {

        boolean win = true; 

        for (int i = 0; i < this.n; i++) {
            if (this.board[row][i] != this.currentPlayerMark) {
                win = false;
                break;
            }
        }

        if (win) return win; 

        win = true; 

        for (int i = 0; i < this.n; i++) {
            if (this.board[i][col] != this.currentPlayerMark) {
                win = false;
                break;
            }
        }

        if (win) return win;

        if (row == col) {
            win = true;

            for (int i = 0; i < this.n; i++) {
                if (this.board[i][i] != this.currentPlayerMark) {
                    win = false;
                    break;
                }
            }

            if (win) return win;
        }

        if ((row + col) == (this.n - 1) ) {

            win = true; 

            for (int i = 0; i < this.n; i++) {

                if (this.board[i][this.n - 1 - i] != this.currentPlayerMark) {
                    win = false;
                    break;
                }
            }

            if (win) return win;
        }

        return false;
    }

    
}

class AlreadyTakenException extends Exception {

    private static final long serialVersionUID = 1L;

    public AlreadyTakenException() {
        super("this cell has been taken!");
    }
}

class BoardFullException extends Exception {

    private static final long serialVersionUID = 1L;

    public BoardFullException() {
        super("board is full!");
    }
}

class GameEndException extends Exception {

    private static final long serialVersionUID = 1L;

    public GameEndException() {
        super("game is end!");
    }
}