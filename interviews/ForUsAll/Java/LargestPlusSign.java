import java.util.HashSet;
public class LargestPlusSign {
    public static void main(String[] args) {
        
        Solution solution = new Solution(); 

        int[][] mines = {{4,2}}; 
        System.out.println(solution.orderOfLargestPlusSign(5, mines));
    }
}

class Solution {
    public int orderOfLargestPlusSign(int N, int[][] mines) {
        
        HashSet<Integer> banned = new HashSet<Integer>(); 
        
        for (int[] mine : mines) {
            
            banned.add(mine[0] * N + mine[1]); 
        }
        
        int[][] dp = new int[N][N]; 
        
        int ans = 0, count; 
        
        for (int r = 0; r < N; r++) {
            count = 0; 
            for (int c = 0; c < N; c++) {
                count = banned.contains(r * N + c) ? 0 : count + 1; 
                dp[r][c] = count;
            }
            
            count = 0;
            for (int c = N - 1; c >= 0; c--) {
                count = banned.contains(r * N + c) ? 0 : count + 1; 
                dp[r][c] = Math.min(dp[r][c], count); 
            }
        }
        
        for (int c = 0; c < N; c++) {
            
            count = 0; 
            
            for (int r = 0; r < N; r++) {
                count = banned.contains(r * N + c) ? 0 : count + 1; 
                dp[r][c] = Math.min(dp[r][c], count);
            }
            
            count = 0;
            for (int r = N - 1; r >= 0; r--) {
                count = banned.contains(r * N + c) ? 0 : count + 1; 
                dp[r][c] = Math.min(dp[r][c], count);
                ans = Math.max(ans, dp[r][c]);
            }
        }
        
        return ans;
    }
}