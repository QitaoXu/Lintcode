import java.util.*;

public class Maze {

    int[][] directions = {{0, 1}, {1, 0}};

    public static void main(String[] args) {

        int[][] grid = new int[4][4]; 
        grid[0][1] = 1; 
        grid[2][2] = 1; 
        grid[2][3] = 1;

        Maze maze = new Maze();

        for (Point p : maze.getPath(grid)) {

            String pos = p.x.toString() + ", " + p.y.toString();

            System.out.println(pos);
             
        }
    }

    public List<Point> getPath(int[][]grid) {

        List<Point> path = new ArrayList<>();
        
        path.add(new Point(0, 0));

        if (this.dfs(grid, path, 0, 0)) {

            return path;
        }

        return new ArrayList<Point>();

    }

    private boolean dfs(int[][] grid, List<Point> path, int x, int y) {

        if (x == (grid.length - 1) && y == (grid[0].length - 1)) {

            return true;
        }

        for (int i = 0; i < 2; i++) {

            int dx = directions[i][0];
            int dy = directions[i][1]; 

            if (!this.isValid(grid, x + dx, y + dy)) 
                continue; 

            Point neighbor = new Point(x + dx, y + dy); 

            path.add(neighbor); 

            if (this.dfs(grid, path, x + dx, y + dy)) 
                return true;

            path.remove(path.size() - 1);

        }

        return false;
    }
                            

    private boolean isValid(int[][]grid, int x, int y) {

        int m = grid.length; 
        int n = grid[0].length; 

        if (x < 0 || x >= m || y < 0 || y >= n) return false; 

        if (grid[x][y] == 1) return false; 

        return true;
    }
}

class Point {

    Integer x; 
    Integer y; 

    public Point(int x, int y) {
        this.x = x; 
        this.y = y; 
    }
}