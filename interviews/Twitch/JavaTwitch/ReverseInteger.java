import java.util.*;
public class ReverseInteger {
    public int reverse(int x) {
        
        int num = x;
        
        List<Integer> digits = getDigits(num);
        
        long res = 0;
        
        for (Integer digit : digits) {
            
            res = res * 10 + digit;
            
        }
        
        if (res > Integer.MAX_VALUE || res < Integer.MIN_VALUE) {
            return 0;
        }
        
        return (int)res;
        
    }
    
    private List<Integer> getDigits(int num) {
        
        List<Integer> digits = new ArrayList<Integer>(); 
        
        if (num == 0) {
            
            digits.add(0); 
            return digits;
            
        }
        
        while (num != 0) {
            
            int digit = num % 10; 
            
            digits.add(digit);
            
            num = num / 10; 
        }
        
        return digits;
        
    }
}