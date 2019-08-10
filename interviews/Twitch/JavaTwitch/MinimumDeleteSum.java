public class MinimumDeleteSum {
    public int minimumDeleteSum(String s1, String s2) {
        
        int m = s1.length(), n = s2.length();
        
        int[][] dp = new int[m + 1][n + 1];
        
        int sum = 0; 
        
        for (int i = 0; i < m; i++) {
            sum += s1.codePointAt(i);
        }
        
        for (int j = 0; j < n; j++) {
            sum += s2.codePointAt(j);
        }
        
        for (int i = 1; i < m + 1; i++) {
            for (int j = 1; j < n + 1; j++) {
                
                
                if (s1.charAt(i - 1) == s2.charAt(j - 1)) {
                    
                    dp[i][j] = Math.max(s1.codePointAt(i - 1) + dp[i - 1][j - 1], Math.max(dp[i - 1][j], dp[i][j - 1]));
                
                }
                
                else {
                    
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }
        
        return sum - 2 * dp[m][n];
        
    }
}