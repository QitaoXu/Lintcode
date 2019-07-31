import java.util.*; 
public class PalinInteger {
    public boolean isPalindrome(int x) {
        
        if (x < 0) return false; 
        
        if (x == 0) return true;
        
        List<Integer> reverseDigits = getReverseDigits(x);
        
        int reverseX = 0; 
        
        for (Integer digit : reverseDigits) {
            
            reverseX = reverseX * 10 + digit;
        }
        
        return reverseX == x;
        
    }
    
    private List<Integer> getReverseDigits(int num) {
        
        List<Integer> reverseDigits = new ArrayList<Integer>();
        
        while (num > 0) {
            
            int digit = num % 10; 
            
            reverseDigits.add(digit);
            
            num = num / 10;
        }
        
        return reverseDigits;
    }
}