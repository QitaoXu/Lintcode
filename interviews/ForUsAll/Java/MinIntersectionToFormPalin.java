public class MinIntersectionToFormPalin{

    public int getMinIntersectionToPalin(String s) {

        int lcs = this.lcs(s, this.reverse(s)); 

        System.out.println(lcs);

        return s.length() - lcs;
    }

    private int lcs(String s1, String s2) {

        int m = s1.length();
        int n = s2.length(); 

        int[][] dp = new int[m + 1][n + 1]; 

        for (int i = 1; i < m + 1; i++) {
            for (int j = 1; j < n + 1; j++) {

                if (s1.charAt(i - 1) == s2.charAt(j - 1) ) 
                    dp[i][j] = dp[i - 1][j - 1] + 1;

                else  
                    dp[i][j] = Math.max(dp[i][j - 1], dp[i - 1][j]); 
            }
        }

        return dp[m][n];
    }

    private String reverse(String s) {

        StringBuilder sb = new StringBuilder(); 

        for (int i = s.length() - 1; i >= 0; i--) {
            sb.append(s.charAt(i));
        }

        return sb.toString();
    }

    public static void main(String[] args) {

        MinIntersectionToFormPalin mitfp = new MinIntersectionToFormPalin(); 

        System.out.println(mitfp.getMinIntersectionToPalin("geeks"));
    }


}