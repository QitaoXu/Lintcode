import java.util.*; 
public class Atoi {
    public int myAtoi(String str) {
        
        str = str.trim();
        
        char[] string = str.toCharArray(); 
        
        if (string.length == 0) return 0;
        
        if (!Character.isDigit(string[0]) && string[0] != '+' && string[0] != '-') 
            return 0;
        
        long res = 0; 
        
        if (Character.isDigit(string[0])) {
            
            for (int i = 0; i < string.length; i++) {
                
                if (!Character.isDigit(string[i])) break;
                
                res = res * 10 + string[i] - '0';
                
                if (res > Integer.MAX_VALUE) return Integer.MAX_VALUE;
            }
        }
        
        else if (string[0] == '+') {
            
            for (int i = 1; i < string.length; i++) {
                
                if (!Character.isDigit(string[i])) break;
                
                res = res * 10 + string[i] - '0';
                
                if (res > Integer.MAX_VALUE) return Integer.MAX_VALUE;
            }
        }
        
        else {
            for (int i = 1; i < string.length; i++) {
                
                if (!Character.isDigit(string[i])) break;
                
                res = res * 10 + string[i] - '0';
                
                if (-res < Integer.MIN_VALUE) return Integer.MIN_VALUE;
            }
            
            res = -res;
            
        }
        
        return (int)res;
        
    }
}