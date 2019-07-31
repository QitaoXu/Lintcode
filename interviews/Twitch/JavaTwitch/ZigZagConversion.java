import java.util.*;

public class ZigZagConversion {
    public String convert(String s, int numRows) {
        
        if (numRows == 1) return s; 
        
        List<StringBuilder> rows = new ArrayList<>(); 
        
        for (int i = 0; i < Math.min(numRows, s.length()); i++) {
            rows.add(new StringBuilder());
        }
        
        int curtRow = 0; 
        boolean goingDown = false; 
        
        for (Character c : s.toCharArray()) {
            
            rows.get(curtRow).append(c);
            
            if (curtRow == 0 || curtRow == rows.size() - 1) goingDown = !goingDown; 
            
            curtRow += goingDown ? 1 : -1;
            
        }
        
        StringBuilder res = new StringBuilder(); 
        
        for (StringBuilder row : rows) {
            res.append(row);
        }
        
        return res.toString();
        
    }
}