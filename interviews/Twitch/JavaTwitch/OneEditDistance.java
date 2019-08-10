public class OneEditDistance {
    public boolean isOneEditDistance(String s, String t) {
        
        if (s.length() == 0 || t.length() == 0) {
            return Math.max(s.length(), t.length()) == 1;
        }
        
        int m = s.length(), n = t.length();
        
        int[][] dp = new int[m + 1][n + 1];
        
        for (int i = 0; i < m + 1; i++) {
            dp[i][0] = i;
        }
        
        for (int j = 0; j < n + 1; j++) {
            dp[0][j] = j;
        }
        
        for (int i = 1; i < m + 1; i++) {
            for(int j = 1; j < n + 1; j++) {
                
                if (s.charAt(i - 1) == t.charAt(j - 1)) {
                    
                    dp[i][j] = dp[i - 1][j - 1];
                }
                
                else {
                    
                    dp[i][j] = Math.min(Math.min(dp[i - 1][j], dp[i][j - 1]), dp[i - 1][j - 1]) + 1;
                }
            }
        }
        
        return dp[m][n] == 1;
    }
}