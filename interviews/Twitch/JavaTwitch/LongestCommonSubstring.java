public class LongestCommonSubstring {
    /**
     * @param A: A string
     * @param B: A string
     * @return: the length of the longest common substring.
     */
    public int longestCommonSubstring(String A, String B) {
        // write your code here
        
        if (A == null || B == null || A.length() == 0 || B.length() == 0) {
            return 0;
        }
        
        int m = A.length(), n = B.length();
        
        int[][] dp = new int[m + 1][n + 1];
        int res = 0; 
        
        for (int i = 1; i < m + 1; i++) {
            for (int j = 1; j < n + 1; j++) {
                
                if (A.charAt(i - 1) == B.charAt(j - 1) ) {
                    
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                    res = Math.max(dp[i][j], res);
                }
                
                else {
                    
                    dp[i][j] = 0;
                }
            }
        }
        
        return res;
    }
}