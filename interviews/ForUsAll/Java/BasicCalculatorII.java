import java.util.*;

public class BasicCalculatorII {
    public int calculate(String s) {
        
        if (s == null || s.length() == 0) {
            return 0;
        }
        
        int len = s.length();
        
        char sign = '+';
        int num = 0; 
        
        Stack<Integer> stack = new Stack<>(); 
        
        for (int i = 0; i < len; i++) {
            
            if (Character.isDigit(s.charAt(i))) num = num * 10 + s.charAt(i) - '0';// digit
            
            if ( (!Character.isDigit(s.charAt(i)) && s.charAt(i) != ' ') || i == len - 1) {
                
                if (sign == '-') stack.push(-num);
                
                if (sign == '+') stack.push(num);
                
                if (sign == '*') stack.push(stack.pop() * num);
                
                if (sign == '/') stack.push(stack.pop() / num);
                
                sign = s.charAt(i);
                num = 0;
            }
            
        }
        
        int re = 0;
        
        for (Integer n : stack) {
            re += n;
        }
        
        return re;
    }
}