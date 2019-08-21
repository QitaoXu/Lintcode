public class Candy {
    public int candy(int[] ratings) {
        
        int[] candies = new int[ratings.length];
        
        Arrays.fill(candies, 1); 
        
        for (int i = 1; i < ratings.length; i++) {
            
            if (ratings[i] > ratings[i - 1]) {
                candies[i] = candies[i - 1] + 1;
            }
        }
        
        int res = 0;
        
        for (int i = ratings.length - 1; i > 0; i--) {
            
            res += candies[i];
            if (ratings[i] < ratings[i - 1] && candies[i] >= candies[i - 1] ) {
                candies[i - 1] = candies[i] + 1;
            }
        }
        
        
        return res + candies[0];
        
    }
}