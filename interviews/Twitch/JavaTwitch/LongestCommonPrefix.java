import java.util.*; 
public class LongestCommonPrefix {
    public String longestCommonPrefix(String[] strs) {
        
        if (strs == null || strs.length == 0) return "";
        
        return lcpHelper(strs, 0, strs.length - 1);
        
    }
    
    private String lcpHelper(String[] strs, int start, int end) {
        
        if (start >= end) return strs[start]; 
        
        int mid = start + (end - start) / 2; 
        
        String leftLcp = lcpHelper(strs, start, mid); 
        String rightLcp = lcpHelper(strs, mid + 1, end);
        
        return commonPrefix(leftLcp, rightLcp);
    }
    
    private String commonPrefix(String left, String right) {
        
        for (int i = 0; i < Math.min(left.length(), right.length()); i++) {
            
            if (left.charAt(i) != right.charAt(i)) 
                return left.substring(0, i);
        }
        
        return left.substring(0, Math.min(left.length(), right.length()));
    }
}