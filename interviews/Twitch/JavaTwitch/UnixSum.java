import java.util.*;

public class UnixSum {

    public static void main(String[] args) {

        String s = "AAAAA"; 

        ArrayList<String> substrings = new ArrayList<>();
        ArrayList<Integer> unix = new ArrayList<>();
        int totalUnix = 0;

        HashMap<String, Integer> memo = new HashMap<>();

        UnixSum unixSum = new UnixSum();

        for (int i = 0; i <= s.length() - 1; i++) {
            for (int j = i + 1; j <= s.length(); j++) {

                substrings.add(s.substring(i, j));
                unix.add(unixSum.getUnix(s.substring(i, j), memo));
                totalUnix += unixSum.getUnix(s.substring(i, j), memo);
            }
        }

        System.out.println(substrings);
        System.out.println(unix);
        System.out.println(totalUnix);
    }

    private int getUnix(String s, HashMap<String, Integer> memo) {

        if (memo.containsKey(s)) return memo.get(s);

        boolean[] characters = new boolean[26]; 

        for (int i = 0; i < s.length(); i++) {

            characters[s.charAt(i) - 'A'] = true;
        }

        int count = 0;

        for (int i = 0; i < 26; i++) {

            if (characters[i] == true) count++;
        }

        memo.put(s, count);
        return count;
    }

}

class TrieNode {

    HashMap<Character, TrieNode> children; 
    boolean isWord; 

    public TrieNode(){
        
        this.children = new HashMap<Character, TrieNode>();
        this.isWord = false;
    }
}

class Trie {

    TrieNode root; 

    public Trie() {

        this.root = new TrieNode();
    }

    public void insert(String word) {

        TrieNode node = this.root; 

        for (int i = 0; i < word.length(); i++) {

            if (!node.children.containsKey(word.charAt(i))) {

                node.children.put(word.charAt(i), new TrieNode());
            }

            node = node.children.get(word.charAt(i));
        }

        node.isWord = true;
    }  
    
    private TrieNode find(String word) {

        TrieNode node = this.root; 

        for (int i = 0; i < word.length(); i++) {

            if (!node.children.containsKey(word.charAt(i))) {

                return null;
            }

            node = node.children.get(word.charAt(i));
        }

        return node;
    }

    public boolean search(String word) {

        TrieNode node = this.find(word);

        return node != null && node.isWord == true;
    }

    public boolean startsWith(String prefix) {

        TrieNode node = this.find(prefix);

        return node != null;
    }

    public ArrayList<String> findAllString() {

        ArrayList<String> results = new ArrayList<>();

        StringBuilder sb = new StringBuilder();

        this.dfs(this.root, sb, results);

        return results;
    }

    private void dfs(TrieNode node, StringBuilder sb, ArrayList<String> results) {

        for (Character c : node.children.keySet()) {

            sb.append(c);
            results.add(sb.toString());
            this.dfs(node.children.get(c), sb, results);
            sb.deleteCharAt(sb.length() - 1);
        }

    }

}

