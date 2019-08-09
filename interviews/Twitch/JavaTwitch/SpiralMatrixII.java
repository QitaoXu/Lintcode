public class SpiralMatrixII {
    public int[][] generateMatrix(int n) {
        
        int[][] matrix = new int[n][n];
        
        int row = n, col = n; 
        int x = 0, y = 0; 
        
        int counter = 1;
        
        while (row > 0 && col > 0) {
            
            if (row == 1) {
                
                for (int i = 0; i < col; i++) {
                    matrix[x][y++] = counter;
                    counter++;
                }
                break;
            }
            else if (col == 1) {
                
                for (int i = 0; i < row; i++) {
                    matrix[x++][y] = counter;
                    counter++;
                }
                break;
            }
            
            
            // Top - Move Right
            for (int i = 0; i < col - 1; i++) {
                
                matrix[x][y++] = counter;
                counter++;
            }
            
            // Right - Move Down
            for (int i = 0; i < row - 1; i++) {
                matrix[x++][y] = counter;
                counter++;
            }
            
            // Bottom - Move Left
            for (int i = 0; i < col - 1; i++) {
                matrix[x][y--] = counter;
                counter++;
            }
            
            // Left - Move Up
            for (int i = 0; i < row - 1; i++) {
                matrix[x--][y] = counter;
                counter++;
            }
            
            row -= 2;
            col -= 2;
            x += 1;
            y += 1;
        }
        
        return matrix;
    }
}