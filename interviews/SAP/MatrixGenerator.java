import java.util.*;

import java.io.*; 

public class MatrixGenerator {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.close();

        MatrixGenerator mg = new MatrixGenerator(); 
        int[][] matrix = mg.generateMatrix(n); 

        for (int i = 0; i < matrix.length; i++) {

            for (int j = 0; j < matrix[0].length; j++) {

                System.out.print(matrix[i][j]);
                System.out.print(" ");
            }

            System.out.println("\n");
        }
    }

    public int[][] generateMatrix(int n) {

        int[][] matrix = new int[n + 1][n];

        for (int i = 0; i < matrix.length; i++) {
            Arrays.fill(matrix[i], n);
        }

        for (int i = 1; i < n; i++) {

            matrix[i][n - 2] = i;
        }

        return matrix;

    }
}