import java.util.*; 

public class GroupAnagrams {
    public List<List<String>> groupAnagrams(String[] strs) {
        
        Map<String, List<String>> map = new HashMap<>(); 
        
        for (String s : strs) {
            
            char[] str = s.toCharArray();
            
            Arrays.sort(str);
            
            String rep = new String(str);
            
            if (!map.containsKey(rep)) {
                
                map.put(rep, new ArrayList<String>());
            }
            
            map.get(rep).add(s);
        }
        
        List<List<String>> results = new ArrayList<>(map.values());
        
        return results;
        
    }
}