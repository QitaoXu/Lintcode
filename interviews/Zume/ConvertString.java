import java.util.*;

public class Zume{

    public boolean canConvert(String s1, String s2) {

        HashMap<Character, Integer> s1OddHash = this.getOddHash(s1);
        HashMap<Character, Integer> s1EvenHash = this.getEvenHash(s1);
        HashMap<Character, Integer> s2OddHash = this.getOddHash(s2);
        HashMap<Character, Integer> s2EvenHash = this.getEvenHash(s2);

        return s1OddHash.equals(s2OddHash) && s1EvenHash.equals(s2EvenHash);
    }

    private HashMap<Character, Integer> getOddHash(String s) {

        HashMap<Character, Integer> oddHash = new HashMap<>();  

        for (int i = 0; i < s.length(); i++) {
            
            if (i % 2 == 0) continue; 
            
            char c = s.charAt(i); 

            if (!oddHash.containsKey(c)) oddHash.put(c, 0);

            oddHash.put(c, oddHash.get(c) + 1);
        }

        return oddHash;
    }

    private HashMap<Character, Integer> getEvenHash(String s) {

        HashMap<Character, Integer> evenHash = new HashMap<>(); 

        for (int i = 0; i < s.length(); i++) {

            if (i % 2 == 1) continue; 

            char c = s.charAt(i);

            if (!evenHash.containsKey(c)) evenHash.put(c, 0); 

            evenHash.put(c, evenHash.get(c) + 1);
        }
        
        return evenHash;
    }
}