public class BestTimeToBuyAndSellStockII {
    public int maxProfit(int[] prices) {
        
        int i = 0; 
        if (prices == null || prices.length == 0) 
            return 0; 
        int valley = prices[0];
        int peak = prices[0];
        int maxprofit = 0;  
        
        while (i < prices.length - 1) {
            
            while (i < prices.length - 1 && prices[i] >= prices[i + 1]) {
                i += 1;
            }
            
            valley = prices[i];
            
            while (i < prices.length - 1 && prices[i] <= prices[i + 1]) {
                
                i += 1;
            }
            
            peak = prices[i];
            maxprofit += peak - valley;
        }
        
        return maxprofit;
    }
}