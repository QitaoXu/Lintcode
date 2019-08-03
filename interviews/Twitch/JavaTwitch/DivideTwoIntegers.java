public class DivideTwoIntegers {
    public int divide(int dividend, int divisor) {
        
        if (dividend == 0) {
            return 0;
        }
        
        if (dividend == Integer.MIN_VALUE && divisor == -1) {
            return Integer.MAX_VALUE;
        }
        
        boolean isNegative = (dividend < 0 && divisor > 0) || 
                             (dividend > 0 && divisor < 0);
                             
        long a = Math.abs((long)dividend);
        long b = Math.abs((long)divisor);
        
        int res = 0; 
        
        while (a >= b) {
            
            int shift = 0; 
            
            while ( a >= (b << shift)) {
                shift += 1;
            }
            
            a -= b << (shift - 1);
            
            res += 1 << (shift - 1);
        }
        
        return isNegative ? -res : res;
        
    }
}