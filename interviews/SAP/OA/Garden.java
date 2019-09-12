import java.io.*;
import java.util.*; 

public class Garden {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in); 
        int n = sc.nextInt();
        System.out.println(n);

        String s = sc.next();
        sc.close();
        System.out.println(s);

        char[][] field = {{'*', '*', '*', '*'}, {'.', '.', '.', '*'}, {'*', '*', '.', '*'}};

        Garden garden = new Garden(); 
        System.out.println(garden.canArrange(field, 1, 1));

    }

    public boolean canArrange(char[][] field, int s, int h) {

        int[] row = new int[field.length]; 
        int[] col = new int[field[0].length]; 
        int flowers = 0; 
        for (int i = 0; i < field.length; i++) {
            for (int j = 0; j < field[0].length; j++) {

                if (field[i][j] == '*') {
                    row[i] += 1;
                    col[j] += 1;
                    flowers += 1;
                }
            }
        }
        
        int rowPart = 0;
        int rowCount = s + 1;
        int rowAverage = flowers / (s + 1);
        boolean rowArrange;

        for (int i = 0; i < row.length; i++) {
            
            rowPart += row[i]; 

            if (rowPart < rowAverage) {
                continue;
            }
            else if (rowPart == rowAverage) {
                rowCount -= 1;
                rowPart = 0;
            }
            else {
                rowArrange = false;
            }
        }

        if (rowPart == 0 && rowCount == 0) {
            rowArrange = true;
        }else {
            rowArrange = false;
        }

        int colPart = 0;
        int colCount = h + 1; 
        int colAverage = flowers / (h + 1);
        boolean colArrange; 

        for (int j = 0; j < col.length; j++) {

            colPart += col[j]; 

            if (colPart < colAverage) {
                continue;
            }
            else if (colPart == colAverage) {
                colCount -= 1;
                colPart = 0;
            }
            else {
                colArrange = false;
            }
        }

        if (colPart == 0 && colCount == 0) {
            colArrange = true;
        }
        else {
            colArrange = false;
        }

        return rowArrange && colArrange;

    }
}