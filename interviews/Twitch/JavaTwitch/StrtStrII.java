public class StrStrII {
    public int strStr(String haystack, String needle) {
        
        String source = haystack, target = needle;
        
        if (source == null || target == null) return -1; 
        
        if (source.equals(target)) return 0;
        
        if (target.length() == 0) return 0;
        
        int targetCode = 0; 
        int base = 100000;
        
        for (int i = 0; i < needle.length(); i++) {
            
            targetCode = (targetCode * 31 + (int)needle.charAt(i)) % base;
        }
        
        int power = 1;
        for (int i = 0; i < needle.length(); i++) {
            
            power = (power * 31) % base;
        }
        
        int hashCode = 0; 
        
        for (int i = 0; i < source.length(); i++) {
            
            hashCode = (hashCode * 31 + (int)source.charAt(i)) % base; 
            
            if (i < target.length()) continue; 
            
            else if (i >= target.length()) {
                
                hashCode = (hashCode - ((int)source.charAt(i - target.length())) * power) % base;
                
                if (hashCode < 0) {
                    hashCode += base;
                }
                
                if (hashCode == targetCode) {
                    
                    if (source.substring(i - target.length() + 1, i + 1).equals(target)) 
                        return i - target.length() + 1;
                }
            }
        }
        
        return -1;
        
    }
}