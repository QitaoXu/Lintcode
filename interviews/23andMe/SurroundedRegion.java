public class SourroundedRegion {
    public void solve(char[][] board) {
        
        if (board == null || board.length == 0 || board[0] == null || board[0].length == 0) {
            return;
        }
        
        int m = board.length;
        int n = board[0].length; 
        
        for (int i = 0; i < m; i++) {
            bfs(board, i, 0);
            bfs(board, i, n - 1);
        }
        
        for (int j = 0; j < n; j++) {
            bfs(board, 0, j);
            bfs(board, m - 1, j);
        }
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                
                if (board[i][j] == 'T') {
                    board[i][j] = 'O';
                }
                
                else if (board[i][j] == 'O') {
                    board[i][j] = 'X';
                }
            }
        }
        
    }
    
    private void bfs(char[][] board, int sx, int sy) {
        
        if (board[sx][sy] != 'O') {
            return;
        }
        
        Queue<Integer> qx = new LinkedList<Integer>();
        Queue<Integer> qy = new LinkedList<Integer>(); 
        
        qx.offer(sx);
        qy.offer(sy);
        
        board[sx][sy] = 'T'; 
        
        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, -1, 1};
        
        while (!qx.isEmpty()) {
            
            int size = qx.size(); 
            
            for (int i = 0; i < size; i++) {
                
                int cx = qx.poll();
                int cy = qy.poll();
                
                for (int j = 0; j < 4; j++) {
                    int nx = cx + dx[j];
                    int ny = cy + dy[j];
                    
                    if (nx < 0 || nx >= board.length || ny < 0 || ny >= board[0].length) {
                        continue;
                    }
                    
                    if (board[nx][ny] != 'O') {
                        continue;
                    }
                    
                    qx.offer(nx);
                    qy.offer(ny);
                    board[nx][ny] = 'T';
                }
            }
        }
        
    }
}