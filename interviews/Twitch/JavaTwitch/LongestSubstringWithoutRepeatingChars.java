import java.util.*; 

public class LongestSubstringWithoutRepeatingChars {

    public int getLongest(String s) {

        int i = 0, j = 0; 
        
        int longest = 0; 
        
        if (s == null || s.length() == 0) return longest;
        
        HashSet<Character> unique = new HashSet<Character>(); 
        
        for (i = 0; i < s.length(); i++) {
            
            while (j < s.length() && !unique.contains(s.charAt(j)) ) {
                
                unique.add(s.charAt(j));
                j++;
            }
            
            longest = Math.max(longest, j - i); 
            
            unique.remove(s.charAt(i));
        }
        
        return longest;
    }
}