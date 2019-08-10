import java.util.*; 
public class SimplifyPath {
    public String simplifyPath(String path) {
        
        List<String> list = new ArrayList<String>();
        
        String[] entries = path.split("/");
        
        for (int i = 0; i < entries.length; i++) {
            
            if (entries[i].length() == 0 || entries[i].equals(".")) {
                continue; 
            }
            
            else if (entries[i].equals("..")) {
                
                if (!list.isEmpty()) {
                    list.remove(list.size() - 1);
                }
                continue;
            }
            else {
                list.add(entries[i]);
            }
        }
        
        StringBuilder sb = new StringBuilder("/");
        
        for (String entry : list) {
            
            sb.append(entry);
            sb.append("/");
        }
        
        if (sb.length() > 1) {
            sb.deleteCharAt(sb.length() - 1);
        }
        
        return sb.toString();
        
        
        
    }
}