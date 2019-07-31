public class longestPalinSubsequence {
    public int getLongestPalindromeSubseq(String s) {
        
        int n = s.length();
        
        if (n == 0) return 0; 
        
        if (n == 1) return 1; 
        
        if (n == 2) {
            
            if (s.charAt(0) == s.charAt(1)) return 2;
            
            else return 1;
        }
        
        int[][] dp = new int[n][n]; 
        
        for (int i = 0; i < n; i++) {
            dp[i][i] = 1; 
        }
        
        for (int i = 0; i < n - 1; i++) {
            
            if (s.charAt(i) == s.charAt(i + 1)) {
                dp[i][i + 1] = 2;
            }
            else {
                dp[i][i + 1] = 1; 
            }
        }
        
        int longest = 0;
        
        for (int diff = 2; diff < n; diff++) {
            
            for (int i = 0; i < n - diff; i++) {
                
                int j = i + diff;
                
                if (s.charAt(i) == s.charAt(j)) {
                    
                    dp[i][j] = dp[i + 1][j - 1] + 2;
                }
                else {
                    
                    dp[i][j] = Math.max(dp[i + 1][j], dp[i][j - 1]);
                }
                
                longest = Math.max(longest, dp[i][j]);
            }
        }
        
        return longest;
        
    }
}