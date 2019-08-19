public class BestTimeToBuyAndSell {
    public int maxProfit(int[] prices) {
        
        int maxDiff = 0; 
        
        if (prices == null || prices.length == 0) 
            return maxDiff;
        
        int min = prices[0]; 
        
        for (int i = 1; i < prices.length; i++) {
            
            maxDiff = Math.max(prices[i] - min, maxDiff);
            min = Math.min(prices[i], min);
        }
        
        return maxDiff;
    }
}