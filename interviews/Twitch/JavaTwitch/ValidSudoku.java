public class ValidSudoku {
    public boolean isValidSudoku(char[][] board) {
        
        boolean[] visited = new boolean[9];
        
        for (int i = 0; i < 9; i++) {
            
            Arrays.fill(visited, false);
            
            for (int j = 0; j < 9; j ++) {
                
                if (!process(board[i][j], visited)) 
                    return false;
            }
            
        }
        
        for (int j = 0; j < 9; j++) {
            
            Arrays.fill(visited, false);
            
            for (int i = 0; i < 9; i++) {
                
                if (!process(board[i][j], visited))
                    return false;
            }
        }
        
        for (int i = 0; i < 9; i += 3) {
            for (int j = 0; j < 9; j += 3) {
                
                Arrays.fill(visited, false);
                
                for (int k = 0; k < 9; k++) {
                    
                    if (!process(board[i + k / 3][j + k % 3], visited)) 
                        return false;
                }
            }
        }
        
        return true;
    }
    
    private boolean process(char cell, boolean[] visited) {
        
        if (cell == '.') return true;
        
        int num = cell - '0';
        
        if (num < 1 || num > 9 || visited[num - 1]) return false;
        
        visited[num - 1] = true;
        
        return true;
        
        
    }
}