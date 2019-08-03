public class CountAndSay {
    public String countAndSay(int n) {
        
        String s = "1";
        
        int i = 2;
        
        while (i <= n) {
            s = readString(s);
            i+= 1;
        }
        
        return s;
        
    }
    
    public String readString(String s) {
        
        char[] string = s.toCharArray();
        
        int count = 0; 
        
        String res = "";
        
        for (int i = 0; i < s.length(); i++) {
            
            if (i == 0 || string[i] == string[i - 1]) {
                count += 1;
            }
            else {
                
                res += count + "" + string[i - 1];
                count = 1;
            }
        }
        
        res += count + "" + string[string.length - 1];
        return res;
    }
}