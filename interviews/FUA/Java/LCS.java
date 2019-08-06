public class LCS {

    public int longestCommonSubsequence(String s1, String s2) {

        if (s1 == null || s1.length() == 0 || s2 == null || s2.length() == 0) {
            return 0;
        }

        int m = s1.length();
        int n = s2.length();

        int[][] dp = new int[m + 1][n + 1]; 

        for (int i = 1; i < m + 1; i++) {
            for (int j = 1; j < n + 1; j++) {

                if (s1.charAt(i - 1) == s2.charAt(j - 1)) 

                    dp[i][j] = dp[i - 1][j - 1] + 1;

                else  
                    dp[i][j] = Math.max(dp[i][j - 1], dp[i - 1][j]); 

            }
        }

        return dp[m][n];
    }

    public static void main(String args[]) {

        String s1 = "abcd";
        String s2 = "abiiiicd"; 

        LCS lcs = new LCS();

        System.out.println(lcs.longestCommonSubsequence(s1, s2));
        System.out.println(3 / 10);
    }
}