public class SpiralMatrix {
    public List<Integer> spiralOrder(int[][] matrix) {
        
        List<Integer> results = new ArrayList<Integer>();
        
        if (matrix == null || matrix.length == 0 || matrix[0] == null || matrix[0].length == 0) {
            return results;
        }
        
        int m = matrix.length, n = matrix[0].length; 
        
        int x = 0, y = 0; 
        
        while (m > 0 && n > 0) {
            
            if (m == 1) {
                
                for (int i = 0; i < n; i++) {
                    results.add(matrix[x][y++]);
                }
                break;
            }
            
            else if (n == 1) {
                
                for (int i = 0; i < m; i++) {
                    results.add(matrix[x++][y]);
                }
                break;
                
            }
            
            // top - move right 
            for (int i = 0; i < n - 1; i++) {
                
                results.add(matrix[x][y++]);
            }
            
            // right - move down 
            for (int i = 0; i < m - 1; i++) {
                results.add(matrix[x++][y]);
            }
            
            // bottom - move left 
            for (int i = 0; i < n - 1; i++) {
                results.add(matrix[x][y--]);
            }
            
            // left - move up
            for (int i = 0; i < m - 1; i++) {
                results.add(matrix[x--][y]);
            }
            
            m -= 2;
            n -= 2; 
            x++;
            y++;
        }
        
        return results;
        
        
    }
}