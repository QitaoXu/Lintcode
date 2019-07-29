import java.util.*;

public class MazePath{

    public List<Point> findMazePath(int[][]maze, Point start, Point end) {

        HashSet<Point> seen = new HashSet<>(); 
        List<Point> path = new ArrayList<Point>(); 

        seen.add(start);

        if (this.dfs(maze, start, end, path, seen)) 

            return path;

        return new ArrayList<Point>();
    }

    private boolean dfs(int[][]maze, Point curt, Point end, List<Point>path, HashSet<Point> seen) {

        if (curt.equals(end)) {
            return true;
        }

        for (Point neighbor : this.getNeighbors(maze, curt)) {

            if (!this.isValid(maze, neighbor)) continue;

            seen.add(neighbor);
            path.add(neighbor);

            if (this.dfs(maze, neighbor, end, path, seen)) {
                return true;
            }

            path.remove(path.size() - 1);
            seen.remove(neighbor);

        }
        return false;
    }
}

class Point{

    int x; 
    int y; 

    public Point(int x, int y) {

        this.x = x; 
        this.y = y; 
    }
}