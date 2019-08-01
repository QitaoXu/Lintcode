public class GenerateParentheses {
    public List<String> generateParenthesis(int n) {
        
        List<String> results = new ArrayList<String>();
        
        int left = n, right = n; 
        
        StringBuilder sb = new StringBuilder();
        
        dfs(left, right, sb, results);
        
        return results;
    }
    
    private void dfs(int left, 
                        int right,
                        StringBuilder sb, 
                        List<String> results) {
        
        if (left == 0 && right == 0) {
            results.add(sb.toString());
            return; 
        }
        
        if (left > 0) {
            
            sb.append('(');
            dfs(left - 1, right, sb, results);
            sb.deleteCharAt(sb.length() - 1);
        }
        
        if (right > 0 && left < right) {
            
            sb.append(')');
            dfs(left, right - 1, sb, results);
            sb.deleteCharAt(sb.length() - 1);
        }
    }
}