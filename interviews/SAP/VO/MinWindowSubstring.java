public class MinWindonSubstring {
    public String minWindow(String s, String t) {
        
        
        int[] sourceHash = new int[256];
        int[] targetHash = new int[256]; 
        
        int targetNum = 0;
        
        for (int i = 0; i < t.length(); i++) {
            
            targetHash[t.charAt(i)] += 1;
            
            if (targetHash[t.charAt(i)] == 1) {
                targetNum += 1;
            }
        }
        
        int l = 0,  r = 0; 
        int ansl = -1, ansr = -1; 
        int sourceNum = 0; 
        
        for (l = 0; l < s.length(); l++) {
            
            while (r < s.length() && sourceNum < targetNum) {
                
                sourceHash[s.charAt(r)] += 1; 
                
                if (sourceHash[s.charAt(r)] == targetHash[s.charAt(r)]) {
                    sourceNum += 1;
                }
                
                r += 1;
                
            }
            
            if (sourceNum == targetNum) {
                
                if (ansl == -1 || r - l < ansr - ansl) {
                    
                    ansl = l;
                    ansr = r;
                }
            }
            
            sourceHash[s.charAt(l)] -= 1;
            
            if (sourceHash[s.charAt(l)] < targetHash[s.charAt(l)]) {
                sourceNum -= 1;
            }
        }
        
        if (ansl == -1) 
            return "";
        
        else 
            return s.substring(ansl, ansr);
        
    }
}